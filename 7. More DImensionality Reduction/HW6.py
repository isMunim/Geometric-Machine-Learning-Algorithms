# -*- coding: utf-8 -*-
"""
Created on Mon Apr  9 20:20:15 2018

@author: Mustafa Hajij
"""

import matplotlib.pyplot as plt
import networkx as nx
import numpy as np

from time import time
from numpy import linalg as LA
from sklearn import manifold, datasets
from sklearn.decomposition import PCA
from sklearn.metrics import pairwise_distances
from sklearn.neighbors import kneighbors_graph
from matplotlib.ticker import NullFormatter
from mpl_toolkits.mplot3d import Axes3D
from scipy.sparse.csgraph import floyd_warshall

"""
Implement MDS 

How it works:
    Construct a matrix of squares of distances
    Apply Double centering
    Extract d largest positive eigen value/vectors
    D-Dimensional MDS positions are outputted...
    
    takes as input a distance matrix (k by k matrix) and number of component d<n 
"""
def doMDS( distanceMatrix, d):
    '''
    Inputs: distance matrix of a data set
            d desired dimensions of the output
            
    Outputs: X set of coordinates that will draw the dataset in d dimensions
    '''
    #Calculate the square of distance matrix
    distanceMatrixSquared = np.square(distanceMatrix)
    #Get the value of n, the number of points
    numPoints = np.shape(distanceMatrixSquared)[1]
    
    # Applying double centering:
    
    #Create an identity matrix (j) of size n by n
    j1=np.identity(numPoints)
    #Create j' -> Basically an n by n matrix with all values =1
    j1dash=np.ones_like(j1)
    # jSub = j - 1/n
    jSub = j1 - (1/numPoints)
    # Multiplying jSub with the  matrix j' 
    j = np.multiply(jSub,j1dash)
    #Caculating B ->
    # j X P^2 X j X -1/2
    s1= np.matmul(j,distanceMatrixSquared)
    s2= np.matmul(s1,j)
    b = s2 * (-0.5)

    #Calculating the eigen values and vectors of our B
    w,v=LA.eig(b)
    #Ensuring we only have real values and no complex numbers    
    w= np.real(w)
    v= np.real(v)

#    print("First Eigenvector",v[:,0])
#    print("Second Eigenvector",v[:,1])
    
    #Sorting eigen values in descending order and slicing the first d e-values
    idx = w.argsort()[-d:][::-1]   
    w = w[idx]
    v = v[:,idx]
    
    #Creating the diagonal of d eigen values    
    wDiag = np.diag(w)
    #Taking element-wise squareroot of the diagonal of d eigen values
    wDiagSQRT = np.sqrt(wDiag)
    
    #Creating our point cloud in d-dimensions by multiplying eigen vectors with
    #the square root of diagonal of eigen values.    
    X = np.matmul(v,wDiagSQRT)
        
    return X


"""
Implement ISOMAP 

"""
def doISOMAP( pointcloud, d, k):
    '''
    Inputs: an array like pointcloud to perform the isomap on
            d number of dimension to be reduced to
            k number of nearest connected neighbours to explore
    Output: X set of coordinates that will draw the dataset in d dimensions
    '''
    knearestMatrix = kneighbors_graph(X, k, mode='distance')
    distMatrix = floyd_warshall(knearestMatrix)
    
    return doMDS(distMatrix, d)






"""
Helper Functions
"""

def getDistanceMatrix(vector):
    '''
        compute distance matrix between points using euclidean
        distance
    '''
    distance_matrix = pairwise_distances(vector,metric='euclidean',squared=False)
    return distance_matrix


def getDistanceMatrixSquared(vector):
    '''
        compute the square of distance matrix between points using euclidean
        distance
    '''
    distanceMatrixSquared = pairwise_distances(vector,metric='euclidean',squared=True)
    return distanceMatrixSquared



"""
Compare your results to the results from the sklearn example 



I tested and compared the algorithms with n_points = 500, n_neighbor=10 and 
n_component=2

On average, my implementation of MDS is nearly 30% faster 
(on 500 n_points, my MDS takes ~20seconds and the sklearn manifold version 
takes around ~75seconds)

On the otherhand, my implementation of ISOMAP takes nearly 50% more time when
compared with the sklearn implementation. (~30 seconds versus ~15 seconds)
This is probably because of the version of Floyd-Warshall algorithm i use and
the nearest neighbor graph I use. 

Both the algorithms create very similar results as compared to their sklearn
counterpart. With the ISOMAPS being nearly identical.

See the following image for comparison:
https://ibb.co/bEbF8c

"""

"""
Driver Code
source = scikit learn examples

"""
# Next line to silence pyflakes. This import is needed.
Axes3D

n_points = 1000
X, color = datasets.samples_generator.make_s_curve(n_points, random_state=0)
n_neighbors = 10
n_components = 2

fig = plt.figure(figsize=(15, 8))

ax = fig.add_subplot(251, projection='3d')
plt.title("Original Dataset")
ax.scatter(X[:, 0], X[:, 1], X[:, 2], c=color, cmap=plt.cm.Spectral)
ax.view_init(4, -72)

Y=getDistanceMatrix(X)

t0 = time()
myMDS=doMDS(Y,2)
t1 = time()

ax = fig.add_subplot(252)
plt.scatter(myMDS[:, 0], myMDS[:, 1], c=color, cmap=plt.cm.Spectral)
plt.title("my MDS (%.2g sec)" % (t1 - t0))
ax.xaxis.set_major_formatter(NullFormatter())
ax.yaxis.set_major_formatter(NullFormatter())
plt.axis('tight')


t0 = time()
myISOMAP = doISOMAP(X,2,10)
t1 = time()


ax = fig.add_subplot(253)
plt.scatter(myISOMAP[:, 0], myISOMAP[:, 1], c=color, cmap=plt.cm.Spectral)
plt.title("my Isomap (%.2g sec)" % (t1 - t0))
ax.xaxis.set_major_formatter(NullFormatter())
ax.yaxis.set_major_formatter(NullFormatter())
plt.axis('tight')

t0 = time()
mds = manifold.MDS(n_components, max_iter=100, n_init=1)
Y = mds.fit_transform(X)
t1 = time()
ax = fig.add_subplot(257)
plt.scatter(Y[:, 0], Y[:, 1], c=color, cmap=plt.cm.Spectral)
plt.title("Sklearn MDS (%.2g sec)" % (t1 - t0))
ax.xaxis.set_major_formatter(NullFormatter())
ax.yaxis.set_major_formatter(NullFormatter())
plt.axis('tight')

t0 = time()
Y = manifold.Isomap(n_neighbors, n_components).fit_transform(X)
t1 = time()
ax = fig.add_subplot(258)
plt.scatter(Y[:, 0], Y[:, 1], c=color, cmap=plt.cm.Spectral)
plt.title("Sklearn Isomap (%.2g sec)" % (t1 - t0))
ax.xaxis.set_major_formatter(NullFormatter())
ax.yaxis.set_major_formatter(NullFormatter())
plt.axis('tight')


"""
Use the data "S" with PCA and, project and plot the data and explain your observation.



Generally, PCA produces an approximate normal of the point cloud. My
implementation of MDS uses the point cloud to create a similarity matrix and
then essentially performs PCA on the disimilarity matrix. The covariance of 
data (used by the PCA algorithm) and the euclidean distance between data points
(used in MDS) are nearly identical. This is (probably) why the results of the my MDA and 
PCA are very similar.

PCA did not do a very good job of reducing the dimensions of the dataset to 2 
dimensions. There's a lot of overlap of the points and there's not much that 
can be 'analyzed' other than an estimate of the original shape of the data.
PCA was unbale to unwrap the data and completely lay it out for further analysis. 


"""

t0 = time()
pca = PCA(n_components=2)
myPCA = pca.fit_transform(X)
t1 = time()
ax = fig.add_subplot(256)
plt.scatter(myPCA[:, 0], myPCA[:, 1], c=color, cmap=plt.cm.Spectral)
plt.title("PCA (%.2g sec)" % (t1 - t0))
ax.xaxis.set_major_formatter(NullFormatter())
ax.yaxis.set_major_formatter(NullFormatter())
plt.axis('tight')


"""
 Dist matrix from slides
"""
slidesExample = [[0,93,82,133],
                 [93,0,52,60],
                 [82,52,0,111],
                 [133,60,111,0]]

slidesExample=np.array(slidesExample)



