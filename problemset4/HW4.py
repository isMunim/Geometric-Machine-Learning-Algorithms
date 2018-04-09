"""
Created on Tue Feb 20 17:49:51 2018

@author: Mustafa Hajij
"""


import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import ufind as uf #source: https://github.com/deehzee/unionfind/blob/master/unionfind.py

# Import any library you see necessary 
from sklearn.metrics import pairwise_distances
from sklearn.neighbors import radius_neighbors_graph
from scipy.sparse import find
#from ufind import *  
from math import inf
"""

Part 1 point cloud 0-barcode 

"""

# this function is provided to you in case you want to load the data sets I gave to you.
def load_data_from_hd(path): # path must be a string to the location of the file
    
    with open(path) as f:
        names_list = [line.split(',') for line in f if line.strip()]
    f=[]    
    for line in names_list:
        f.append([float(x) for x in line])
    return np.array(f)



def zero_barcode_pointcloud(pointcloud,alpha):
    # 1-Create an ε-neighborhood graph of the distance matrix M
    G = epsilon_neighborhood_graph(pointcloud,alpha)
    #2-Initiate an empty UnionFind U and add graph nodes to it.
    U = uf.UnionFind(G.nodes())
#    U.insert_objects(G.nodes())
    Bi=[] #Empty list to store tuples of node birth/deaths

    for node in G.nodes(data=True):
        Bi.append((0,inf))
    
    zeroBarcode={}
    sortedList=sorted(G.edges(data=True), key=lambda x: x[2]['weight'])

    for ei in sortedList: #For all edges
        if(U.find(ei[0])!= U.find(ei[1])): #Where ei[0] is one node and ei[1] other
            #Getting connected components that each node belongs
            C1 = U.component(ei[0]) 
            C2 = U.component(ei[1])
            #Creating two empty temporary lists
            tempC1 = []
            tempC2 = []
            #Only selecting components that are not dead yet
            for components in C1:
                if Bi[components][1] is inf:
                    tempC1.append(components)
            for components in C2:
                if Bi[components][1] is inf:
                    tempC2.append(components)
                    
            C1 = min(tempC1)
            C2 = min(tempC2)
            #Joining C1 and C2 as nodes in different components
            U.union(C1,C2)
            #Seting the death of B1 to w(ei)
            Bi[C1] = (0, G[ei[0]][ei[1]]['weight'])
            
    #Creating a dictionary with nodes labeled c:
#    for i in range(0, len(G.nodes())):
    for i in G.nodes():
        zeroBarcode[i] = tuple(Bi[i])
            

 
    return zeroBarcode



"""

Part 2 : no code is required. Submit the results as described in the description.

"""
#Dataset 1:
#
#7-Give an estimation of how many connected components probably this data has
#based on 0-persistence diagram
#1 long bar, so the data has one cluster/connected components and rest is noise
#
#8-Does the data have any important(long bars)1-persistence feature?
#Explain your observation.
#Data has one long bar so it probably has one genus 
#
#9-Write down the persistence of the highest 1-feature.
#(Recall that persistence of a bar = death -birth)
#persistence = 1.55-0.2 = 1.35
#
#Dataset 2:
#
#7-Give an estimation of how many connected components probably this data has
#based on 0-persistence diagram
#Since there's only one big line, it is probably 1 cluster/1 connected component
#figure with the rest being noise.
#
#8-Does the data have any important(long bars)1-persistence feature?
#Explain your observation.
#Data has two almost equal long bars. This probably means that the data has 2 genus, probably like an 8.
#
#9-Write down the persistence of the highest 1-feature.
#(Recall that persistence of a bar = death -birth)
#persistence = 1.75-0.5 = 1.25

"""

Part 3 (Bonus)scalar function 0-barcode 

"""

# use the following dataset as an input for this function

pointcloud=[(1,1),(2,2),(3,4),(4,3),(5,5),(6,3.5),(7,7),(8,8),(9,9),(10,8),(11,9.5),(11,7.5),(12,12),(13,1.5)]


def zero_barcode_scalar_functoin(pointcloud,alpha):
    #1.Initiate an empty UnionFind U.
    U = uf.UnionFind()

    #2.Sort with respect the y values.
    sortedcloud = sorted(pointcloud, key=lambda x: x[1])
    m = mapPointCloud(pointcloud,sortedcloud)
    
        
    birth=[]
    pairs=[]
    for point in pointcloud:
        birth.append(0)
#    print(birth)

#    for i in range(0,len(pointcloud)-1):
    for i,val in enumerate(pointcloud):
        if (m[i] is 0): #first point is min because we just sorted
            
            if(sortedcloud[i][1]<pointcloud[m[i]+1][1] or sortedcloud[i][1]==pointcloud[m[i]+1][1]): #Min
                #birth event                
                U.add(i)
                birth[m[i]]=pointcloud[m[i]][1]

            elif(sortedcloud[i][1]>pointcloud[m[i]+1][1]): #Max
                #Death event
                C=U.component(i-1)
                U.add(i)
                C=min(C)
                U.union(C,(i))
                if(birth[m[i]+1] < birth[m[i]]):
                    pairs.append([pointcloud[m[i]], pointcloud[m[i]-1]])
                    birth[m[i]-1]=-1 #Setting birth to -1 to indicate already paired 
                elif(birth[m[i]+1] == birth[m[i]]): #Edge case, haha!
                    pairs.append([pointcloud[m[i]], pointcloud[m[i]-1]])
                    birth[m[i]-1]=-1 #Setting birth to -1 to indicate already paired 
            
        elif (m[i] is len(pointcloud)-1): #last point must be max cause we sorted
        
            if(sortedcloud[i][1]>pointcloud[m[i]-1][1]): #Max
                #Death event
                C=U.component(i-1)
                U.add(i)
                C=min(C)
                U.union(C,(i))
                if(birth[m[i]-1] > birth[m[i]]):
                    pairs.append([pointcloud[m[i]], pointcloud[m[i]-1]])
                    birth[m[i]-1]=-1 #Setting birth to -1 to indicate already paired 
                elif(birth[m[i]-1] == birth[m[i]]): #Edge case, haha!
                    pairs.append([pointcloud[m[i]], pointcloud[m[i]-1]])
                    birth[m[i]-1]=-1 #Setting birth to -1 to indicate already paired 
                    
            elif(sortedcloud[i][1]<pointcloud[m[i]-1][1] or sortedcloud[i][1]==pointcloud[m[i]-1][1]): #Min
                #birth event
                U.add(i)
                birth[m[i]]=pointcloud[m[i]][1]


        elif (sortedcloud[i][1]<pointcloud[m[i]-1][1] and sortedcloud[i][1]<pointcloud[m[i]+1][1]):
            #Birth Event
            U.add(i)
            birth[m[i]]=pointcloud[m[i]][1]
        elif (sortedcloud[i][1]>pointcloud[m[i]-1][1] and sortedcloud[i][1]>pointcloud[m[i]+1][1]):
            #Death event Local Maxima

            C=U.component(i-1)
            U.add(i+1)
            U.add(i)
            C=min(C)
            
            U.union(C,(i+1))
            U.union(C,(i))
            if(birth[m[i]-1] > birth[m[i]+1]):
                pairs.append([pointcloud[m[i]], pointcloud[m[i]-1]])
                birth[m[i]-1]=-1 #Setting birth to -1 to indicate already paired 
            elif(birth[m[i]-1] < birth[m[i]+1]):
                pairs.append([pointcloud[m[i]], pointcloud[m[i]+1]])
                birth[m[i]+1]=-1 #Setting birth to -1 to indicate already paired 
            elif(birth[m[i]-1] == birth[m[i]+1]): #Edge case, haha!
                pairs.append([pointcloud[m[i]], pointcloud[m[i]-1]])
                birth[m[i]-1]=-1 #Setting birth to -1 to indicate already paired                 
        else:
            C=U.component(i-1)
            C=min(C)
            U.union(C,i)
            birth[m[i]]=pointcloud[m[C]][1]

            
        
            
        
#    print(pairs)
#    print(pointcloud)
    return pairs

"""

Helper Functions

"""

def epsilon_neighborhood_graph(pointcloud,alpha):
     
    mat= radius_neighbors_graph(pointcloud,alpha, mode='distance', include_self=False,p = 2)
    (row,col,entries)=find(mat)
    G =nx.Graph()     
    for i in range(0,len(pointcloud)):
        G.add_node(i)
    for i in range(0,len(row)):
        G.add_edge(row[i],col[i],weight=entries[i])
         
    return G    

def findDistanceMatrix(vector):
    '''
        compute distance matrix between points using euclidean
        distance
    '''
    distance_matrix = pairwise_distances(vector,metric='euclidean')
    return distance_matrix

def plotPointCloud(pointcloud):
    parray = np.asarray(pointcloud)
    x,y = parray.T
    plt.scatter(x,y)
    plt.ylabel('some numbers')
    plt.grid(True)
    plt.axis([0, 13, 0, 13])
    plt.show()
    
def mapPointCloud(pointcloud,sortedcloud):
    '''
    Where m[index_in_sorted_pointcloud]=index_in_unsorted_pointcloud
    '''
    m = {} #Map of sorting
    for idP,i in enumerate(pointcloud):
        for idS,j in enumerate(sortedcloud):
            if (i == j):
#                print("Sorted Index "+str(idS)+" Unsorted Index"+str(idP))
                m[idS]=idP
 
    return m
                   
#Test code to see if distance matrix works
#M=findDistanceMatrix(pointcloud)
#print("PointCloud: ")
#print(pointcloud);
#
#print("distance_matrix M: ")
#print(M);                         

alpha = 2.2
print("Our Point Cloud")
print(pointcloud)
print("Running zero barcode on the give point cloud with alpha = "+str(alpha))
myDict=zero_barcode_pointcloud(pointcloud,alpha)
print(myDict)
print("Running scalar zero barcode on the give point cloud to obtain pairs ")
myPairList=zero_barcode_scalar_functoin(pointcloud,alpha)
print(myPairList)




    