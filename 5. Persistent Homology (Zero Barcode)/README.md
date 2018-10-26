### Section 5 -> Persistent Homology

In this section I implement the zero bar code  algorithm for computing topological features of a space at different spatial resolutions.

I implemented two functions:

1. **zero_barcode_pointcloud** to calculate for point clouds
Pseudocode:
Input: A distance matrix M, maximal value ε
Output: 0-barcode of M with max value ε

  1. Create an ε-neighborhood graph of the distance matrix M
  2. Initiate an empty UnionFind U.
  3. for each node vi in G :
    1. U.add(vi)
    2. Create a bar Bi with birth = 0 and death = ∞ (this is just a tuple)
  4. Sort the edges of G in an increasing order
  5. for each edge ei in G do:
    - If ei connects two different sets C1 and C2 then1. Join C1 and C22. Set the death of B1 to w(ei)(this is just the weightof the graph)


2. **zero_barcode_scalar_function** to calculate on a scalar functions.
Pseudocode:
---
