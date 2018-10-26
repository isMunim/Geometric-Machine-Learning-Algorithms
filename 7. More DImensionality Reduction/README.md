### Section 7 --> More Dimensionality Reductiom


In this section I implement my own versions of the:

1. **MDS Algorithm**
How it works:
  - Construct a matrix of squares of distances
  - Apply Double centering
  - Extract d largest positive eigen value/vectors
  - D-Dimensional MDS positions are outputted
This function takes as input a distance matrix (k by k matrix) and number of component d<n

2. **ISOMAP Algorithm**
  How it works:
  1. Construct the neighborhood graph of the data X using the K-NN neighborhoodgraphwe studied earlier in the course.
  2. Use the Dijekstra algorithm or the Floyd–Warshall algorithm to find the distance between nodes on the graph.
  3. Apply MDS on the distance matrix above and extract the coordinates with the desired dimension (part one of the algorithm).

In this section, I also implemented the SciKit Learn versions of the following algorithms:

1. MDS
2. ISOMAP
3. PCA
