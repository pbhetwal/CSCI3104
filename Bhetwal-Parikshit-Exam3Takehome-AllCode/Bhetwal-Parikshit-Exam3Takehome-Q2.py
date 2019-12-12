"""
@author: Rhoenigman
         Shivendra
"""
import networkx as nx
import sys 
"""
The function to generate the input graph

:return: Returns the NetworkX Graph for Q2
"""
def Question2():
    # Create a directed graph
    G = nx.DiGraph()

    # The 'length' on each edge should be ignored and is only for drawing.
    # Adding an edge also adds the node
    
    G.add_edge('EC', 'A', length=40, weight=1.0)
    G.add_edge('EC', 'H', length=40, weight=1.0)
    G.add_edge('EC', 'J', length=60, weight=1.0)

    G.add_edge('H', 'G', length=40, weight=1.0)
    G.add_edge('H', 'K', length=40, weight=1.0)

    G.add_edge('G', 'L', length=40, weight=1.0)
    G.add_edge('G', 'F', length=40, weight=1.0)

    G.add_edge('F', 'E', length=40, weight=1.0)

    G.add_edge('E', 'HUMN', length=40, weight=1.0)

    G.add_edge('J', 'S', length=80, weight=1.0)
    G.add_edge('J', 'K', length=60, weight=1.0)

    G.add_edge('K', 'L', length=40, weight=1.0)
    G.add_edge('L', 'M', length=40, weight=1.0)
    G.add_edge('M', 'N', length=40, weight=1.0)
    G.add_edge('M', 'F', length=60, weight=1.0)

    G.add_edge('N', 'O', length=80, weight=1.0)
    G.add_edge('N', 'E', length=80, weight=1.0)

    G.add_edge('O', 'HUMN', length=40, weight=1.0)

    G.add_edge('A', 'S', length=60, weight=1.0)
    G.add_edge('A', 'B', length=40, weight=1.0)

    G.add_edge('B', 'R', length=40, weight=1.0)
    G.add_edge('B', 'C', length=40, weight=1.0)

    G.add_edge('S', 'R', length=60, weight=1.0)
    G.add_edge('R', 'Q', length=40, weight=1.0)

    G.add_edge('Q', 'C', length=40, weight=1.0)
    G.add_edge('Q', 'P', length=60, weight=1.0)

    G.add_edge('C', 'D', length=40, weight=1.0)
    G.add_edge('D', 'HUMN', length=40, weight=1.0)
    G.add_edge('P', 'D', length=40, weight=1.0)
    G.add_edge('P', 'O', length=60, weight=1.0)
    G.add_edge('O', 'HUMN', length=40, weight=1.0)

    G.add_edge('T', 'Q', length=40, weight=1.0)
    G.add_edge('T', 'P', length=40, weight=1.0)
    G.add_edge('T', 'O', length=40, weight=1.0)
    G.add_edge('T', 'N', length=40, weight=1.0)
    G.add_edge('T', 'M', length=40, weight=1.0)

    G.add_edge('R', 'T', length=40, weight=1.0)
    G.add_edge('S', 'T', length=40, weight=1.0)
    G.add_edge('J', 'T', length=40, weight=1.0)
    G.add_edge('K', 'T', length=40, weight=1.0)
    G.add_edge('L', 'T', length=40, weight=1.0)
    
    return G


"""
A utility function to help visualize the generated graph

:param G: NetworkX Graph
:return: None (instead saves the input graph in .png format)
"""
def draw_graph(G):
    import matplotlib.pyplot as plt
    import pylab
    edge_labels = dict([((u, v,), d['weight'])
                        for u, v, d in G.edges(data=True)])
    node_labels = {node: node for node in G.nodes()}

    pos = nx.spectral_layout(G)
    nx.draw_networkx_labels(G, pos, labels=node_labels)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
    nx.draw(G, pos, node_size=500, edge_cmap=plt.cm.Reds)
    plt.savefig('Finals_Q2_Graph.png')
    pylab.title("Input Graph")
    pylab.show()

def shortestWithKStops(G, k, START, END): 
    """
    This function uses dynamic programming to check if we can get 
    from a vertex, START, to another vertex, END, using exactly 
    k stops and the shortest path. If such a solution exists, 
    it will return a string composed of k, START, END, the path weight,
    and the actual path itself. If such a solution doesn't exist, it 
    will notify the user. 
  
    :param G: (Required) The graph object to traverse  
    :param k: (Required) The number of target stops  
    :param START: (Required) The starting vertex 
    :param END: (Required) The destination vertex 
    :returns sol: A string of relevant information if 
                  a solution is possible 
    :returns notPoss: A string notifying the user 
                      if a solution is not possible 
    """ 
    # Init n, size of nodes 
    s, t, n = 0, 0, len(G.nodes())
    # Closest we can get to infinity 
    MAX = sys.maxsize
    # Hold our nodes in a list 
    SET_NODES = list(G.nodes()) 
    # Source and target indices 
    s = SET_NODES.index(START)
    t = SET_NODES.index(END)

    # Init costs to MAX 
    # M[n][n][k] - each subproblem represents 
    # shortest path from i -> j using k stops 
    M = [[[MAX for _ in range(k+1)]for _ in range(n)]for _ in range(n)]
    # We only want at most k stops
    # so, we iterate for k, checking edges 
    # along the way 
    for K in range(k+1):
        # Let i represent the index of the source 
        # for a given sub-problem 
        for i in range(n):
            # Let j represent the index of the source 
            # for a given sub-problem  
            for j in range(n): 
                # K stops means K + 1 edges 
                # If there is one edge for that sub-problem (i -> j) and i -> j exists
                # Then we store the weight of that edge 
                if(K+1 == 1 and G.has_edge(SET_NODES[i], SET_NODES[j])):
                    M[i][j][K] = G.edges[SET_NODES[i], SET_NODES[j]]['weight']
                # If there is more than one edge  
                elif(K+1 > 1): 
                    # Than we must consider all vertices that are adjacent 
                    for adj in range(n):
                        # If there i and adj are connected 
                        if(G.has_edge(SET_NODES[i], SET_NODES[adj])):
                            # Consider leaving 
                            leave = M[i][j][K]
                            # Consider taking  
                            take = G.edges[SET_NODES[i], SET_NODES[adj]]['weight'] + \
                                   M[adj][j][K-1]
                            # We want the minimum weight 
                            M[i][j][K] = min(leave, take)

    # If gettting from s to t with k stops is not possible 
    if(M[s][t][k] == MAX):
        # Tell the user it is not possible 
        if(k > 1 or k < 1):
            notPoss = "Going from " + START + " to " + END + " with " + str(k) + " stops is not possible.\n"
        elif(k == 1):
            notPoss = "Going from " + START + " to " + END + " with " + str(k) + " stop is not possible.\n"
        return notPoss 
    # Otherwise, backtack 
    PATH = [SET_NODES[t]] 
    # Init l as k and j as the target index 
    l, j = k, t
    # While l is not 0 
    while(l != 0):
        # Loop through the nodes 
        for i in G.nodes():
            # If there is a node that connects to the destination 
            if(i in list(G.predecessors(PATH[len(PATH)-1]))):
                # If the chosen sub-problem was 'take' from sub-problems 
                if(G.edges[i, PATH[len(PATH)-1]]['weight'] + M[s][SET_NODES.index(i)][l-1] == M[s][j][l]): 
                    # Add the node to the path 
                    PATH += [i]
                    # Decrement l
                    l -= 1
                    # Set j to that added node index
                    j = SET_NODES.index(i)
    # Backtracked, so reverse array 
    PATH.reverse()
    # Add source array 
    PATH.insert(0, SET_NODES[s])
    # Create a string with k, source, destination, 
    # the shortest path weight, and the path itself 
    sol = "k: " + str(k) + \
          "\nSource: " + str(START) + \
          "\nDestination: " + str(END) + \
          "\nPath Weight: " + str(M[s][t][k]) + \
          "\nPath: " + ' -> '.join(PATH) + "\n" 
    return sol


def main():
    ################## READ CAREFULLY ##############################

    # Note that you cannot use any networkx functionality
    # which makes the solution trivial

    # The 'length' on each edge (while generating the graph)
    # should be ignored and is only for drawing.
    # You should consider the 'weight' for finding the smallest path.
    # The above example has weights 1 but the weight can be anything.
    # Later on we may post some more graphs for testing.
    G = Question2()
    draw_graph(G)

    # Call your function here that takes in the Graph "G"
    # and returns the shortest path
    # (note that it is not the length but the entire path)
    
    print(shortestWithKStops(G, 0, 'EC', 'HUMN'))
    print(shortestWithKStops(G, 1, 'EC', 'HUMN'))
    print(shortestWithKStops(G, 2, 'EC', 'HUMN'))
    print(shortestWithKStops(G, 3, 'EC', 'HUMN'))
    print(shortestWithKStops(G, 4, 'EC', 'HUMN'))
    print(shortestWithKStops(G, 5, 'EC', 'HUMN'))
    print(shortestWithKStops(G, 6, 'EC', 'HUMN'))
    print(shortestWithKStops(G, 7, 'EC', 'HUMN'))
    print(shortestWithKStops(G, 8, 'EC', 'HUMN'))
    print(shortestWithKStops(G, 9, 'EC', 'HUMN'))
    print(shortestWithKStops(G, 6, 'EC', 'E'))

if __name__ == "__main__":
    # The driver function
    main()
