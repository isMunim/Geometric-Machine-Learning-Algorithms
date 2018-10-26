#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 14 18:02:14 2018

@author: Mustafa Hajij and Munim Zahid
"""

from unionfind import *
import networkx as nx

class kruskalsalgorithm():
    def __init__(self,inputgraph):
        self.original_graph=inputgraph
        self.tree=nx.Graph()


    # uncomment the following function and start your implementation as described in lecture 2
    def spanningtree(self):
        '''
        Let G=(V,E,w)
        Pseudocode:
        A= {}
        foreach v∈V:
            MAKE-SET(v)
        foreach (u, v) in E ordered by weight(u, v), increasing:
            if FIND-SET(u) ≠FIND-SET(v):
                A=A∪{(u,v)}
                UNION(u, v)
            return A
        '''
        #Sorting the graph in Ascending order

        #print(self.original_graph.edges(data=True)) TEST
        sortedList=sorted(self.original_graph.edges(data=True), key=lambda x: x[2]['weight'])


        #Creating UnionFind objects
        uf = UnionFind()
        uf.insert_objects(self.original_graph.nodes())



        #mst=nx.Graph() already created in constructor
        for u,v,w in sortedList: #foreach (u, v) in E
            w=w.get('weight') #getting rid of the keys
            if(uf.find(u)!= uf.find(v)): #if FIND-SET(u) ≠FIND-SET(v)
                self.tree.add_edge(u,v, weight=w) #Creating the new tree
                uf.union(u,v) #UNION(u, v)
        #print(self.tree.edges(data=True)) DEBUG code
        return self.tree #return A
