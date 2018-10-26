### Section 3 --> Clustering Algorithms

Here's a list of algorithms implemented in this section

1. **BFS.py**
This file contains two functions.
  * **BFS:**
  This is a classic [breadth first search](https://en.wikipedia.org/wiki/Breadth-first_search) algorithm.

  * **BFS_graph_connected_components**:
  This function used the BFS function to return the connected components of a networkx graph object.
  This is identical to the following networkx [function][1]
2. **emst.py**
This is my implementation of the **Euclidean Minimum Spanning Tree** algorithm.
It function that takes as an input a collection of points 𝑋 = [𝑝1,…,𝑝𝑛] and returns the Euclidian minimum spanning tree of X.
It utilizes the kruskals algorithm made in section 2.
Here's how the algorithm is implemented:
```
  -> Compute the complete graph on the points 𝑝1,…,𝑝𝑛.
  Use the distance between the points as the weight of
  the edges of the complete graph.

  -> Run the Kruskal’s algorithm implemented in section 1
  on the complete graph you obtained in step 1.
```
3. **zahn.py**
This function implements Zahn's Clustering Algorithm. It takes as an input a collection of points 𝑋 = [𝑝1,…,𝑝𝑛] and a number of clusters 𝑘 and returns back k clusters of the 𝑋 using Zahn’s clustering algorithm. The points 𝑝*i* can be in any Euclidian space 𝑅^𝑑.
Here's how the algorithm is implemented:
```
-> Compute the EMST of X.
-> Sort the edges of EMST(X) in decreasing order.
-> Delete the longest k-1 edges of EMST(X).
-> Return the k connected components (clusters) of the
   resulting forest.
```
4. **epsilon.py**
This file contains two functions:
   * **epsilon_graph:**
   This function created the epsilon graph of a point cloud.
   It takes as an input a collection of points 𝑋 = [𝑝1,…,𝑝𝑛] and a positive real number 𝜀 ≥ 0  and returns the ε-neighborhood graph.

   * **epsilon_graph_clusters:**
   This function takes as an input a collection of points 𝑋 = [𝑝1,…,𝑝𝑛] and a positive real number 𝜀 ≥ 0  and returns the clusters induced by the connected components of the **ε-neighborhood graph**.

*unionfind.py* provides the necessary data structure.
*graph.py* is the driver file which can be used to test all of these algorithms.

To test and run:
``` python
python3 graph.py
```
inside graph.py, X is defined as collection of points!



[1]: https://networkx.github.io/documentation/networkx-1.9.1/reference/generated/networkx.algorithms.components.connected.connected_components.html#networkx.algorithms.components.connected.connected_components
