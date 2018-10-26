import networkx as nx
import numpy as np
from kruskalsalgorithm import *

#collectionOfPoints = [(0,1),(0,2),(1,3),(1,4),(2,5),(2,6),(2,8),(6,7)]
#
# def makeGraph(collectionOfPoints):
#     i=0
#     while (i < len(collectionOfPoints)) :
#         C.add_node(i,pos=collectionOfPoints[i])
#         i=i+1
#     # for(i=0, i<len(self)-1, i++):
#     #     x=self[i]
#     #     y=self[i+1]
#     #     weight =  math.sqrt(sum([(a - b) ** 2 for a, b in zip(x, y)]))
#     #     emstGraph=nx.Graph()
#     #     emstGraph.add_node(i,pos=collectionOfPoints[i],weight=math.sqrt(sum([(a - b) ** 2 for a, b in zip(x, y)])))
#     i=1
#     while (i < len(collectionOfPoints)-1) :
#         x=collectionOfPoints[i]
#         y=collectionOfPoints[i+1]
#         print(str(x)+","+str(y))
#         weight =  math.sqrt(sum([(a - b) ** 2 for a, b in zip(x, y)]))
#         C.add_edge(i,i+1,weight=weight)
#         i=i+1
#
# def makeCompleteGraph(emstGraph,createUsing=none):
#     S= networkx.empty_graph(len(emstGraph),create_using)
#     if len(L)>1:
#         if emstGraph.is_directed():
#             edges = itertools.permutations(L,2)
#         else:
#             edges = itertools.combinations(L,2)
#         emstGraph.add_edges_from(edges)
#     return emstGraph

def emst(X):
    #print(X)
    emstGraph=nx.Graph()

    for z in X:
        emstGraph.add_node(z)
    # #emstGraph.add_nodes_from(X)
    # i=0
    # while (i < len(X)) :
    #     emstGraph.add_node(1)
    #     i=i+1

    for x in emstGraph.nodes():
        for y in emstGraph.nodes():
            if (x!=y):
                emstGraph.add_edge(x,y)
    for i in X:
        for j in X:
            if(np.any(i!=j)):
                w = np.linalg.norm(np.array(i)-np.array(j))
                emstGraph.add_edge(tuple(i),tuple(j), weight=w)
    # print("EMST before kruskals")
    #
    # for edge in emstGraph.edges():
    #     a=edge[0]
    #     b=edge[1]
    #     print("edge "+str(edge)+" has  weight " + str(emstGraph[a][b]['weight']) )

    k = kruskalsalgorithm(emstGraph)
    return k.spanningtree()
