from collections import defaultdict

from sklearn.cluster import SpectralClustering as SpectralClusteringAlgorithm # Algorithm
import matplotlib.pyplot as plt
import numpy as np
import numpy as np
from sklearn.preprocessing import MinMaxScaler

np.set_printoptions(threshold=np.inf)


# matplotlib.use('MacOSX')
def dist3D(p1, p2):
    p1 = np.array(p1)
    p2 = np.array(p2)
    squared_dist = np.sum((p1 - p2) ** 2, axis=0)
    return np.sqrt(squared_dist)

def makeCenterClusterList(vectors_3dim,k,sc):
    CenterClusterList = list()
    nodeDevidedByCluster = defaultdict(list)
    for i,node in enumerate(vectors_3dim):
        nodeDevidedByCluster[sc.labels_[i]].append(node)

    for i in range(k):
        nodeDevidedByCluster[i] = np.array(nodeDevidedByCluster[i])
        sum = np.array([0, 0, 0])
        for node in nodeDevidedByCluster[i]:
            sum = sum + np.array(node)
        sum = sum / len(nodeDevidedByCluster[i])
        CenterClusterList.append(sum)
    return CenterClusterList

def generateInteria_(vectors_3dim,k,sc):
    CenterClusterList = makeCenterClusterList(vectors_3dim,k,sc)
    CenterPerNode = list()
    for i, node in enumerate(vectors_3dim):
        CenterPerNode.append(CenterClusterList[sc.labels_[i]])
    CenterPerNode = np.array(CenterPerNode)
    inertia_ = 0  # Sum of squared distances of samples to their cluster center.
    for i in range(len(CenterPerNode)):
        inertia_ = inertia_ + (dist3D(vectors_3dim[i], CenterPerNode[i])) ** 2
    return inertia_

class SpectralClustering:
    def __init__(self, vectors_3dim, df, color):
        self.vectors_3dim = vectors_3dim
        self.df = df
        self.color = color
        self.sc = SpectralClusteringAlgorithm(n_clusters=self.find_elbow(), assign_labels="discretize",n_init=10, random_state=0)
        self.sc.fit_predict(self.vectors_3dim)

    def find_elbow(self):

        mms = MinMaxScaler()
        mms.fit(self.vectors_3dim)
        data_transformed = mms.transform(self.vectors_3dim)

        Sum_of_squared_distances = []
        # K = range(1, int(0.01 * len(data_transformed)))
        K = range(6, 18)
        for i, k in enumerate(K):
            sc = SpectralClusteringAlgorithm(n_clusters=k)
            sc = sc.fit(self.vectors_3dim)
            Sum_of_squared_distances.append(generateInteria_(self.vectors_3dim,k,sc))
            if (len(Sum_of_squared_distances)) > 1:
                gradient = Sum_of_squared_distances[i] - Sum_of_squared_distances[i - 1]
                if gradient > -1200:
                    return k - 1
        # plt.plot(K, Sum_of_squared_distances, 'bx-')
        # plt.xlabel('k')
        # plt.ylabel('Sum_of_squared_distances')
        # plt.title('Elbow Method For Optimal k')
        # plt.show()

    def getPlot(self):

        # Create a scatter plot
        base_figure = plt.figure(dpi=120, figsize=(160, 100)).gca(projection='3d')
        base_figure.scatter(
            xs=self.df["pca-one"],
            ys=self.df["pca-two"],
            zs=self.df["pca-three"],
            s=1
        )


        base_figure.scatter(self.vectors_3dim[:,0] , self.vectors_3dim[:, 1], self.vectors_3dim[:, 2], s=1,c=self.sc.labels_, depthshade=False)

        base_figure.set_xlabel('x axis')
        base_figure.set_ylabel('y axis')
        base_figure.set_zlabel('z axis')
        return plt
