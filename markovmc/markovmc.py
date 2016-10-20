def grapher(x,N):
    import networkx as nx
    from random import choice
    import math
    G=nx.complete_graph(len(x))
    for item in G.edges():
        G[item[0]][item[1]]['weight']= math.hypot(x[item[1]-1][0] - x[item[0]-1][0], x[item[1]-1][1] - x[item[0]-1][1])
         
        
    H=G
    for i in list(range(N)):
        random_node = choice(G.nodes())
        random_node_2 = choice(G.nodes())
        if random_node == random_node_2:
            random_node_2 = choice(G.nodes())
        edge = (random_node,random_node_2)
        if edge in nx.edges(G):
            G.remove_edge(edge[0],edge[1])
        else:
            G.add_edge(edge[0],edge[1])
        
    return G
