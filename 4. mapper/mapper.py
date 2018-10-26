"""
Created on Tue Feb 20 17:49:51 2018

@author: Munim Zahid
"""

import networkx as nx

from sklearn.neighbors import radius_neighbors_graph
from scipy.sparse import find

import random
import numpy as np
import math


class interval():
    def __init__(self,_a,_b):
         self.a=_a
         self.b=_b


def epsilon_neighborhood_graph(pointcloud,alpha):

    mat= radius_neighbors_graph(pointcloud,alpha, mode='distance', include_self=False,p = 2)
    (row,col,entries)=find(mat)
    G =nx.Graph()
    for i in range(0,len(pointcloud)):

        G.add_node(i)
    for i in range(0,len(row)):

        G.add_edge(row[i],col[i],weight=entries[i])

    return G

def epsilon_graph_clusters(pointcloud,alpha): # you will need this inside the main function mapper_graph

    graph=epsilon_neighborhood_graph(pointcloud,alpha)

    CC_graphs=list(nx.connected_component_subgraphs(graph))

    CC_points=[]

    for CC in CC_graphs:

        CC_points.append([pointcloud[i] for i in CC.nodes()])
    return CC_points


def circle_example(number): # this function just samples from the unit circle uniformaly.


    X=[]
    for i in range(0,number):
        angle = random.uniform(0,1)*(math.pi*2)
        x=math.cos(angle)
        y=math.sin(angle)
        X.append((x,y))

    return X


def build_coordiante_filter(X,coordinate): # this creates a simple f to be used as input for the function

    f={}
    for x in X:

        f[x]=x[1]  #this maps  (x,y) in the circle to the coordinate y

    return f





"""
INTERVAL is an instance of the class provided above.
Technically you can calculate that from the function f
("a" would be the min value of f and "b" would be the max value of f )

"""

def calculate_cover(INTERVAL,N,epsilon):  #INTERVAL =[a,b] , N is number of divisions for the interval and epsilon is the overlap
    listCover=[] #list of covers to be returned
    coverElem=INTERVAL.a #setting first element of first cover to be interval.a
    difference=INTERVAL.b-INTERVAL.a #calculating range of our interval
    jumps=difference/N #calculating jump value between each slice

    while coverElem < INTERVAL.b:
        tempCover=[] #Creating a temporary list, to be insterted into our list of covers
        if(coverElem==INTERVAL.a): #base case 1: starting element must be interval.a
            tempCover.append(coverElem)
            tempCover.append((coverElem+jumps)+(0.5*epsilon))
        elif((coverElem+jumps)==INTERVAL.b): #base case 1: last element must be interval.b
            tempCover.append((coverElem)-(0.5*epsilon))
            tempCover.append((coverElem+jumps))
        else: #default cases
            tempCover.append((coverElem)-(0.5*epsilon))
            tempCover.append((coverElem+jumps)+(0.5*epsilon))
        coverElem=coverElem+jumps #incrementing the cover by the slice
        listCover.append(tempCover) #appending the list into our list of lists.

    #Let's flatten our list of lists to a list.....
    #listCover = [item for sublist in listCover for item in sublist]
    return listCover
    #return a list of intervals each of them represents part of the cover as described in the lecture.

"""
Input mapper_graph:
X is an array that represents the data. Each element point must be a tuple : otherwise Python will complain when you want to use the function f for hashing the points in X.
f is a dictionary : keys are the points in X and the values are real numbers
N is the number of slices in the cover
epsilon : is the amount of overlap between slices
alpha is the clustering parameter for the function epsilon_graph_clusters provided above

"""

def mapper_graph(X,f,N,epsilon,alpha):


        """
    0-Using the function f to calculate a=min(f(x)) and to calculate b=max(f(x)). You obtain the interval [a,b].
    1-Run the function calculate_cover(the interval [a,b], N,epsilon) to calculate the cover and store that in a list U=[ U_1,…,U_N].
	2-For each cover element, U_i in U find the elements in X that map via f into this  U_i. Store that in a bucket say  V_i.  At the end of this process you will obtain a list V=[ V_1,…,V_N].
	3-Create an empty list and name it ALL_CLUSTERS. This container will contain all the clusters that we will calculate

	4-For each set V_i run the clustering algorithm epsilon_graph_clusters(V_i,alpha) provided to you in the file. This is exactly the same clustering algorithm you did in problem set 2. Store the clusters. The output of this function is a collection of clusters associated to V_i. You need to insert those clusters inside the list ALL_CLUSTERS.

	5-After you finish doing (4) for every V_i  in V,the list in ALL_CLUSTERS will be something like ALL_CLUSTERS =[C_1,….,C_K].

	6-Create an empty graph G

	7-For every cluster C_i  in ALL_CLUSTERS create in a node in G

	8-Create a nested for loop and go over the clusters in ALL_CLUSTERS:

        a-check if C_i intersection C_j is not empty: if this is the case insert an edge between the node i and the node j.
	return the graph G

        """

        #step 0
        minX=min(f.values())
        maxX=max(f.values())
        #step 1
        INTERVAL = interval(minX, maxX)
        U=calculate_cover(INTERVAL,N,epsilon)
        #step 2
        V=[]
        #V=np.array()
        for sublist in U:
            tempV=[]
            for x in X:
                if f[x] >= sublist[0] and f[x] <= sublist[1]:
                    tempV.append(list(x))
            V.append(tempV)
        #step 3
        ALL_CLUSTERS = []
        #step 4
        for sublist in V:
            if(len(sublist)!=0):
                ALL_CLUSTERS.append(epsilon_graph_clusters(sublist, alpha))
        #step 5 verification
#        for clusters in ALL_CLUSTERS:
#            print("cl")
#            clusters = [item for sublist in clusters for item in sublist]
#            print(clusters)

        #Step 6
        G=nx.Graph()
        index=0
        #Step 7

        for i,clusters in enumerate(ALL_CLUSTERS):
            #Flattening cluster list
            clusters = [item for sublist in clusters for item in sublist]
            node = clusters[int(len(clusters)/2)]
            G.add_node(index, pos=tuple(node), clust=i)
            index=index+1
        #step 8
        edgesList=[[0,index-1]]
        for index1, i in enumerate(ALL_CLUSTERS):
            #tuple_of_tuples = tuple(tuple(x) for x in list_of_lists)
            i=[item for sublist in i for item in sublist]
            i=[tuple(l) for l in i]
            i=tuple(i)
            for index2,j in enumerate(ALL_CLUSTERS):
                if(index2>index1):
                    j=[item for sublist in j for item in sublist]
                    j=[tuple(l) for l in j]
                    j=tuple(j)
                    if(i!=j):
                        if (not set(i).isdisjoint(set(j))):
                            tempList=[index1,index2]

                            edgesList.append(tuple(tempList))


        graphNodesPos= nx.get_node_attributes(G,'pos')
        G.add_edges_from(edgesList)
#        nx.draw(G,pos=nx.spring_layout(G))
#        nx.draw(G,pos=graphNodesPos)
        return G

"""
test your work
"""

# (1) define the data
X=circle_example(1000)

# (2) define the function f
f=build_coordiante_filter(X,1) # this will create a function f(x,y)=y

#print("X is")
#print(X)
#
#print("F is ")
#print(f)
#
#print("F(x) is")
#print(f[X[1]])
#
#minX=min(f.values())
#print("minX> ")
#print(minX)
#maxX=max(f.values())
#print("maxX> ")
#print(maxX)

# choose other Mapper parameters : I choose the following. You will need to keep
changing them untill you obtain the a good result (circular graph)

N=6
epsilon=0.1 # this will also depend on the number of points in X
alpha=0.15 # this will depend on the number of points in X


#testing calculate_cover
myInterval = interval(0,1)

#myList=calculate_cover(myInterval,N,epsilon)
#print(myList)

# (3) run the Mapper constructoin
G=mapper_graph(X,f,N,epsilon,alpha)

# (4) Draw the grpah using networkx

#nx.draw(G)
nx.draw(G,pos=nx.spring_layout(G))

# (5) save the output image
