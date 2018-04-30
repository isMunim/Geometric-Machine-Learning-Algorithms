# -*- coding: utf-8 -*-
"""
Created on Mon Apr  9 20:20:15 2018

@author: Mustafa Hajij
"""

import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
import pandas as pd

from sklearn.manifold import MDS
from sklearn.manifold import spectral_embedding as SE
"""
Use the following function to draw a graph
the following function accepts as input a graph G
and a dictionary pos

pos is the position of the nodes of the graph G

"""
def getDistanceMatrix(graph):
    '''
        compute distance matrix of a weighted graph
        Input: Graph G
        Output: NP array where dimension = 
                        [number of egdes in G x number of egdes in G ]
        Dependencies: pandas DataFrame (see pandas.pydata.org)
    '''
    pathLengths = dict(nx.all_pairs_dijkstra_path_length(graph))
    df = pd.DataFrame(pathLengths)
    distanceMatrix = df.as_matrix()
    return distanceMatrix

def setWeight(graph,val):
    '''
        Sets weight of each edge to the value provided if the graph is
        unweighted
        Input: Graph G
               Value to assing to all edges in G
        Output: none
        Dependencies: networkx
    '''
    for edge in graph.edges():
        a=edge[0]
        b=edge[1]
        if(G.get_edge_data(a,b) == {} ): #Checks if graph is unweighted
            graph.add_edge(a, b, weight=val) #Sets graph weight to input val
        

def getGraphInfo(graph):
    '''
        Prints info of graph for debugging
    '''
    for edge in graph.edges():
        a=edge[0]
        b=edge[1]
        if(G.get_edge_data(a,b) == {} ):
            print("no weight")    
        else:
            print("edge "+str(edge)+" has  weight " + str(graph[a][b]['weight']) )

def draw_graph(G,pos): # this function is provided for you and you do not need to alter it.
     
     nx.draw_networkx_nodes(G, pos,
                       node_color='r',
                       node_size=500,
                       alpha=1)
     nx.draw_networkx_edges(G, pos, width=1.0, alpha=0.5)

#example of utilization of the above function

#(1) Define the graph G

G = nx.cubical_graph()

#(2) check the nodes of the graph G

print("the nodes of the graph are : ")
print(G.nodes())

#(3) define the position dictionary
pos = {0: np.array([ 0.82877618,  0.53211873]), 
       1: np.array([ 0.8059564,  0.       ]), 
       2: np.array([ 0.51148475,  0.37349706]), 
       3: np.array([ 0.54462887,  0.89200482]), 
       4: np.array([ 0.31695909,  0.62593525]), 
       5:np.array([ 0.02260257,  1.        ]), 
       6: np.array([ 0.        ,  0.46707769]), 
       7: np.array([ 0.28222528,  0.10714391])}

print("the position of the nodes of the graph are : ")
print(pos)

# draw the graph 

#draw_graph(G,pos)



# start your code here

#(I)

# the input of both of the following two functions is a weighted graph G. (In case the graph is not weighted you should make sure to assign a weight of 1 to the edges)
# the output is a dictionary of positions that assigns to everynode in the graph a position as in the above example


def graph_node_position_mds(G): 
    #Setting weight of all edges to 1 if graph is unweighted (skips otherwise)
    setWeight(G,1)
    
    #Caclulating distance/dissimilarity matrix and storing in an ndarray
    distMat = getDistanceMatrix(G);
    print(distMat)
    #Running sklearn.manifold.MDS on the matrix
    MDS_pos = MDS(n_components=2,dissimilarity='precomputed').fit_transform(distMat)
    
#    print(MDS_pos) prints ndarray
    #Declaring empty dictionary to store the MDS node positions
    MDS_pos_dict = {}
    #Storing MDS node positions in the dict
    for nodeIndex, val in enumerate(MDS_pos):
        MDS_pos_dict[nodeIndex]=val

    return MDS_pos_dict

def graph_node_position_Laplacian(G):
    #Setting weight of all edges to 1 if graph is unweighted (skips otherwise)
    setWeight(G,1)
    
    #Caclulating distance/dissimilarity matrix and storing in an ndarray
    distMat = getDistanceMatrix(G);
    
    #Running sklearn.manifold.spectralembedding on the matrix
    SE_pos = SE(distMat, n_components=2)
    
#    print(SE_pos) prints ndarray
    #Declaring empty dictionary to store the MDS node positions
    SE_pos_dict = {}
    #Storing MDS node positions in the dict
    for nodeIndex, val in enumerate(SE_pos):
        SE_pos_dict[nodeIndex]=val
    return SE_pos_dict



#(II) test your results :
    #A    
        # (1 ) run the function  graph_node_position_mds and save the results as MDS_pos
        # (2 ) run the function draw_graph(G,MDS_pos)
  
    # B 
        # (1 ) run the function graph_node_position_Laplacian and save the results as Laplacian_pos
        # (2 ) run the function draw_graph(G,Laplacian_pos)
   
#Test A
    
MDS_pos = graph_node_position_mds(G);
print("the position of the nodes of the graph's MDS are : ")
print(MDS_pos)
draw_graph(G,MDS_pos)

#Test B
        
#Laplacian_pos = graph_node_position_Laplacian(G);
#print("the position of the nodes of the graph's laplacian are : ")
#print(Laplacian_pos)
#draw_graph(G,Laplacian_pos)

#NOTES

#To print 2d dict one by one
#for x in length:
#    print (x)
#    for y in length[x]:
#        print (y,':',length[x][y])
