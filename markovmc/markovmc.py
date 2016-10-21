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
    from random import choice
    import math
    graphs = []
    G = nx.complete_graph(len(x))
    for i in list(range(N)):
        H = G
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
        theta_g = theta(G, r)
        theta_h = theta(H, r)
        fx = math.exp(-(theta_g-theta_h)/T)
        b_g = 0
        b_h = 0
        for i in nx.degree(G):
            if nx.degree(G)[i] == 1:
                b_g += 1
        for i in nx.degree(H):
            if nx.degree(H)[i] == 1:
                b_h += 1
        q_h_g = 1/(len(x)*(len(x)-1)/2-b_h)
        q_g_h = 1/(len(x)*(len(x)-1)/2-b_g)
        # print lines for classical debugging
        # print(1/(len(x)*(len(x)-1)/2-b_h))
        # print(len(x))
        # print(b_h)
        # print(q_h_g)
        aij = fx*q_g_h/q_h_g
        if aij > 1:
            graphs.append(G)
        else:
            graphs.append(H)
    return graphs


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
