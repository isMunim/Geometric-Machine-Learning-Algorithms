import math
import networkx as nx
import itertools
import numpy as np
#from unionfind import *
from kruskalsalgorithm import *
from BFS import *
from emst import emst
from zahn import zahn
from epsilon import *

G=nx.Graph()
nodesList = [0,1,2,3,4,5,6,7,8]
G.add_nodes_from(nodesList)
G.add_edges_from([(0,1),(0,2),(1,2),(2,3),(1,3),(1,4),(5,6),(6,7)])

B=nx.Graph()
B.add_nodes_from(nodesList)
B.add_edges_from([(0,1),(0,2),(1,3),(1,4),(2,5),(2,6),(2,8),(6,7)])

X = [(0,1),(0,2),(1,3),(1,4),(2,5),(2,6),(2,8),(6,7)]
#X = [(1,2),(2,0),(3,1),(1,1),(0,4)]


print("Running BFS from 0")
print(bfs(G,0))

print("Running BFS_graph_connected_components")
print(BFS_graph_connected_components(G))

print("Connected Components using nx.connected_components")
print(sorted(nx.connected_components(G), key = len, reverse=True))

newEmstTree = emst(X)
print("EMST")
for edge in newEmstTree.edges():
    a=edge[0]
    b=edge[1]
    print("edge "+str(edge)+" has  weight " + str(newEmstTree[a][b]['weight']) )
#print(newEmstTree.edges())


print("Zahn's Algo with k=2: ")
print(zahn(X,2))

newEpsilonTree = epsilon_graph(X,2)
print("Epsilon Graph with e=2")
for edge in newEpsilonTree.edges():
    a=edge[0]
    b=edge[1]
    print("edge "+str(edge)+" has  weight " + str(newEpsilonTree[a][b]['weight']) )

#print(newEpsilonTree.edges())

print("Epsilon Graph Clusters with e=2 ")
print(epsilon_graph_clusters(X,2))
