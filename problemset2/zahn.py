from emst import emst
import networkx as nx
import numpy as np
from BFS import *

def zahn(X,k):
    emstTree = emst(X)
    sortedEMST =  nx.Graph()
    for z in X:
        sortedEMST.add_node(z)
    sortedList=sorted(emstTree.edges(data=True), key=lambda x: x[2]['weight'], reverse=True)

    # print ("Before")
    # print (sortedEMST.edges())
    # print("list")
    # print (sortedList)

    i=0
    while (i < (k-1)):
        del sortedList[0]
        i=i+1
    # print("After delete")
    # print (sortedEMST.edges())
    # print("list")
    # print (sortedList)

    sortedEMST.add_edges_from(sortedList)

    # print("Zahn")
    # for edge in sortedEMST.edges():
    #     a=edge[0]
    #     b=edge[1]
    #     print("edge "+str(edge)+" has  weight " + str(sortedEMST[a][b]['weight']) )
    #
    # print (sortedList)
    # print(sortedEMST.edges(data=True))
    #return BFS_graph_connected_components(sortedEMST)
    return sorted(nx.connected_components(sortedEMST), key = len, reverse=True)
