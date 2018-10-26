from emst import emst
import networkx as nx
import numpy as np
from BFS import *


def epsilon_graph(X, e):
    epsilonGraph=nx.Graph()

    for z in X:
        epsilonGraph.add_node(z)

    # for x in epsilonGraph.nodes():
    #     for y in epsilonGraph.nodes():
    #         if (x!=y):
    #             epsilonGraph.add_edge(x,y)

    for i in X:
        for j in X:
            if(np.any(i!=j)):
                w = np.linalg.norm(np.array(i)-np.array(j))
                if(w <= e):
                    epsilonGraph.add_edge(tuple(i),tuple(j), weight=w)
                elif (epsilonGraph.has_edge(tuple(i),tuple(j))):
                    epsilonGraph.remove_edge(tuple(i),tuple(j))

    return epsilonGraph

def epsilon_graph_clusters(X,e):
    epsilonGraph=epsilon_graph(X,e)
    return sorted(nx.connected_components(epsilonGraph), key = len, reverse=True)
