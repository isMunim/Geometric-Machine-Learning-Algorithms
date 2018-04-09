# -*- coding: utf-8 -*-
"""
Created on Thu Jan 18 16:39:14 2018

@author: Mustafa Hajij

"""
import networkx as nx
from unionfind import *
from kruskalsalgorithm import *

# Load a graph example from networkx
graph=nx.house_x_graph()

print("The nodes of the graph are given by the list : ")
print(graph.nodes())
print("The edges of the graph are given by the list : ")
print(graph.edges())

# here we are giving weights to the edges
initweight=1
for edge in graph.edges():
    graph.add_edge(edge[0], edge[1], weight=initweight)
    initweight=initweight+1

# check the weights of the edges:
for edge in graph.edges():
    a=edge[0]
    b=edge[1]
    print("edge "+str(edge)+" has  weight " + str(graph[a][b]['weight']) )

#print(graph.edges(data=True))
'''
To check if our program sorts, use code below to 'unsort' the graph
'''
#First, we mess (sh)it up
# graph.remove_edge(0,1)
# graph.add_edge(0,1,weight=10)

# #Sorting the graph
# sortedList=sorted(graph.edges(data=True), key=lambda x: x[2]['weight'])


k = kruskalsalgorithm(graph)
mst = k.spanningtree()


print("Minimnal Spanning Tree:")
for edge in mst.edges():
    a=edge[0]
    b=edge[1]
    print("edge "+str(edge)+" has  weight " + str(mst[a][b]['weight']) )

# now you will need to calculate the minimal spanning tree for the graph above.

# Implement Kruskal algorothm and run it on the above graph example and record your result.
