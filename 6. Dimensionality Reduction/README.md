### Section 6 --> Dimensionality Reduction

In this section, I implement two dimensionality reduciton algorithms to ease
graph drawing.

- **MDS** based node position

  *My Pseudocode:*  
  Input: A weighted graph G(V,E).
  If the graph is unweighted, assign a weight of 1 to every edge.
  Output: a dictionary that assigns to every node v in V a position np.array(x,y).
    1. Compute the distance matrixDof the graph G
    2. Use sklearn [MDS][1] function on the distance D and specify the n_components=2.Make sure your input is a distance matrix and not a point cloud (the default is a pointcloud).
    3. Get the position you obtained from MDS and save them in a dictionary as illustratedin the attached file (HW5.py)
    4. Return the dictionary of the positions



- **Laplacian** based node position [Spectral Embedding]

  *My Pseudocode:*
  Input: A weighted graph G(V,E).
  If the graph is unweighted, assign a weight of 1 to every edge.
    1. Compute the distance matrixDof the graph G
    2. Use sklearn [spectral embedding][2] function on the distance D and specify the n_components=2
    3. Get the positionsyou obtained from spectral embedding output and save them in a dictionary
    4. Return the dictionary of the positions





[1]: http://scikit-learn.org/stable/modules/generated/sklearn.manifold.MDS.html
[2]: http://scikit-learn.org/stable/modules/generated/sklearn.manifold.spectral_embedding.html#sklearn.manifold.spectral_embedding
