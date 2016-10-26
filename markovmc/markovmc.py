def grapher(x, N, r, T):
    '''This function is a Markoc Chain Monte Carlo Simulator.
    Parameters
    ----------
        x : list of tuples
            cartesian location of nodes
        N : int
            number of iterations
        r : int
            adjustable parameter
        T : int
            adjustable Parameters
    Returns
    -------
    graphs : list
             most likely graphs from each iteration
    '''
    import networkx as nx
    from random import choice, random
    import math
    graphs = []
    G = nx.cycle_graph(len(x))
    for i in list(range(N)):
        H = nx.Graph()
        I = nx.Graph()
        J= nx.Graph()
        for edge in nx.edges(G):
            H.add_edge(edge[0], edge[1])
            J.add_edge(edge[0], edge[1])
        for item in H.edges():
            del_x = x[item[1]-1][0] - x[item[0]-1][0]
            del_y = x[item[1]-1][1] - x[item[0]-1][1]
            weight = math.hypot(del_x, del_y)
            H[item[0]][item[1]]['weight'] = weight
        random_node = choice(G.nodes())
        random_node_2 = choice(G.nodes())
        if random_node == random_node_2:
            random_node_2 = choice(G.nodes())
        edge = (random_node, random_node_2)
        if edge in nx.edges(G):
            G.remove_edge(edge[0], edge[1])
            if not nx.is_connected(G):
                G.add_edge(edge[0], edge[1])
        else:
            G.add_edge(edge[0], edge[1])
        for item in G.edges():
            del_x = x[item[1]-1][0] - x[item[0]-1][0]
            del_y = x[item[1]-1][1] - x[item[0]-1][1]
            weight = math.hypot(del_x, del_y)
            G[item[0]][item[1]]['weight'] = weight
            I.add_edge(item[0], item[1])
        theta_g = theta(G, r)
        theta_h = theta(H, r)
        fx = math.exp(-(theta_g-theta_h)/T)
        b_g = 0
        b_h = 0
        for i in G.edges():
            I.remove_edge(i[0],i[1])
            if not nx.is_connected(I):
                b_g +=1
                I.add_edge(i[0], i[1])
            else:
                I.add_edge(i[0], i[1])
        for i in H.edges():
            J.remove_edge(i[0],i[1])
            if not nx.is_connected(J):
                b_h +=1
                J.add_edge(i[0], i[1])
            else:
                J.add_edge(i[0], i[1])
        q_h_g = 1/(len(x)*(len(x)-1)/2-b_h)
        q_g_h = 1/(len(x)*(len(x)-1)/2-b_g)
        # print lines for classical debugging
        # print(1/(len(x)*(len(x)-1)/2-b_h))
        # print(len(x))
        # print(b_h)
        # print(q_h_g)
        aij = fx*q_h_g/q_g_h
        # print(nx.info(G))
        # print(nx.info(H))
        #print(aij)
        # print(fx)
        if aij > random():
            graphs.append(G)
        else:
            graphs.append(H)
    return graphs

def topOnePercent(graphs):
    '''This function determines the top one percent elements that show up most often in a list, implemented for graphs but works with any list.
    Parameters
    ----------
        graphs : list
                 list to be analyzed
    Returns
    -------
    top_one_percent : list
                      most likely graphs 
    '''
    graph_dict = {}
    for i in graphs:
        if i in graph_dict:
            graph_dict[i] += 1
        else: 
            graph_dict[i] = 1
    num = int(len(graph_dict)/100)
    import operator
    sorted_x = sorted(graph_dict.items(), key=operator.itemgetter(1))
    # print(len(graph_dict))
    # print(num)
    top_one_percent = sorted_x[-num:]
    # print(top_one_percent)
    return top_one_percent

def expectedDegree(graphs, node):
    '''This function determines the expected degree for a given node
    Parameters
    ----------
        graphs : list
                 graphs to be analyzed
        node   : int
                 node to be analyzed
                
    Returns
    -------
        mean : float
               expected degree 
    '''
    from statistics import mean
    degreeList = []
    for i in graphs:
        degreeList.append(i.degree(node))
    return mean(degreeList)

def expectedNumberofEdges(graphs):
    '''This function determines the expected number of edges for a given set of graphs
    Parameters
    ----------
        graphs : list
                 graphs to be analyzed
                
    Returns
    -------
        mean : float
               expected number of edges
    ''' 
    from statistics import mean
    edges = []
    for i in graphs:
        edges.append(i.number_of_edges())
    return mean(edges)

def expectedShortestPathLength(graphs, node_a, node_b):
    '''This function determines the expected shortest path for a given set of graphs and two nodes
    Parameters
    ----------
        graphs : list
                 graphs to be analyzed
        node_a : int
                 first node
        node_b : int
                 second node
                
    Returns
    -------
        mean : float
               expected shortest path
    ''' 
    from statistics import mean
    import networkx as nx
    pathList=[]
    for i in graphs:
        pathList.append(nx.dijkstra_path_length(i, node_a, node_b))
    return mean(pathList)

    
def theta(G, r):
    '''This function calculates the relative probability parameter for a graph.
       Called in grapher function.
    Parameters
    ----------
        G : graph
            graph to be analyzed
        r : int
            adjustable parameter
    Returns
    -------
    theta : float
            parameter for probability calculation
    '''
    import networkx as nx
    theta = 0
    if not nx.is_connected(G):
        raise RuntimeError('Disconnected Graph')
    for item in G.edges(data='weight'):
        y = item[2]
        theta += r*y
    for item in G.nodes():
        theta += nx.dijkstra_path_length(G, item, 1)
    return theta
