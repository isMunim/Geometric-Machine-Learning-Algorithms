### Section 2 --> Creating a minimal spanning tree using kruskals algorithm

Here, I implemented kruskals algorithm to generate minimal spanning trees.

There are three main files

1. *kruskalsalgorithm.py*
This file contains my implementation of the algorithm based on the following pseudocode:
```
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
```
2. *unionfind.py*
This file contains a simple implementation for union-find data structure. You will need this file in order to easily implement the Kruskal’s algorithm.

3. *graph_example.py*
This is *technically* the driver file. It has a graph example using networkx. This will get you started using the networkx library. We do not need much beyond knowing how to create a graph, how to add a node and edge to that graph. In this file I am loading a graph example that comes with the package and then list its nodes and edges. I then assigned a weight to the edges of that graph. If you run that file you will see that it prints to you the list of nodes, list of edges and their weights.

---
A tutorial on how to create a graph and add nodes and edges for networkx can be found [here](https://networkx.github.io/documentation/networkx-1.10/tutorial/tutorial.html).
