### Section 4 --> Mapper Algorithm

In this section we implement the [mapper](https://research.math.osu.edu/tgda/mapperPBG.pdf) algorithm for better analysis of high
dimension data sets.

The following secion contains two files. *mapper.py* and *better-mapper.py*.
They both implement the same mapper algorithm using the same strategy. The
better-mapper.py just does the same job in a simpler manner. When implementing,
I found that the mapper.py approach makes one learn more but the second one makes the code more readable.

Input of the Mapper algorithm has 5 parameters:
1. The data X
2. The function f:X->[a,b]
3. N: The number of slices ofthe interval[a,b]
4. The overlap between the slices epsilon
5. The clustering parameter alpha

The output is the Mapper graph.

The algorithm is implemented in two parts.

#### Part 1
**Calculate Cover**:
The function calculate_cover constructs the cover. It takes as an input the following:

1. The interval [a,b]
2. N: The number of slices of [a,b]
3. The overlap between the slices “epsilon”

Thisreturns the slicesU1,...,Un. I will call each such a slice Ui a cover element.
Each cover element Ui must overlap with the next cover element Ui+1by an amount of “epsilon”.

#### Part 2
**Implementing mapper_graph**:
This part implements the mapper algorithm. Here's my pseudocode:

```
  0. Using the function f to calculate a=min(f(x)) and to calculate b=max(f(x)).
     You obtain the interval [a,b].
  1. Run the function calculate_cover(the interval [a,b], N,epsilon) to calculate
     the cover and store that in a list U=[ U_1,…,U_N].
  2. For each cover element, U_i in U find the elements in X that map via f into
     this  U_i. Store that in a bucket say  V_i.  At the end of this process you
     will obtain a list V=[ V_1,…,V_N].
  3. Create an empty list and name it ALL_CLUSTERS. This container will contain
     all the clusters that we will calculate
  4. For each set V_i run the clustering algorithm epsilon_graph_clusters(V_i,alpha)
     provided to you in the file. Store the clusters. The output of this function
     is a collection of clusters associated to V_i. We need to insert those
     clusters inside the list ALL_CLUSTERS.
  5. After you finish doing (4) for every V_i  in V,the list in ALL_CLUSTERS
     will be something like ALL_CLUSTERS =[C_1,….,C_K].
  6. Create an empty graph G
  7. For every cluster C_i  in ALL_CLUSTERS create in a node in G
  8. Create a nested for loop and go over the clusters in ALL_CLUSTERS:
      ->check if C_i intersection C_j is not empty: if this is the case insert
        an edge between the node i and the node j.
  9. return the graph G

```
