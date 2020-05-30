from collections import defaultdict

from matplotlib import pylab
from mpl_toolkits.mplot3d import proj3d
from sklearn.cluster import SpectralClustering as SpectralClusteringAlgorithm # Algorithm
import matplotlib.pyplot as plt
import numpy as np
from sklearn.preprocessing import MinMaxScaler

np.set_printoptions(threshold=np.inf)


# matplotlib.use('MacOSX')

def dist3D(p1, p2):
    p1 = np.array(p1)
    p2 = np.array(p2)
    squared_dist = np.sum((p1 - p2) ** 2, axis=0)
    return np.sqrt(squared_dist)

def makeNodeDevidedByCluster(vectors_3dim,k,sc):
    nodeDevidedByCluster = defaultdict(list)
    for i, node in enumerate(vectors_3dim):
        nodeDevidedByCluster[sc.labels_[i]].append(node)
    for i in range(k):
        nodeDevidedByCluster[i] = np.array(nodeDevidedByCluster[i])
    return nodeDevidedByCluster

def makeCenterClusterList(vectors_3dim,k,sc):
    nodeDevidedByCluster = makeNodeDevidedByCluster(vectors_3dim,k,sc)
    CenterClusterList = list()
    for i in range(k):
        sum = np.array([0, 0, 0])
        for node in nodeDevidedByCluster[i]:
            sum = sum + np.array(node)
        sum = sum / max(len(nodeDevidedByCluster[i]), 1)
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
    def __init__(self, vectors_3dim, color, arrow_size):
        self.vectors_3dim = vectors_3dim
        self.color = color
        k = 8#self.find_elbow()
        self.sc = SpectralClusteringAlgorithm(n_clusters=k, assign_labels="discretize",n_init=10, random_state=0)
        self.sc.fit_predict(self.vectors_3dim)
        # create the centers of the clusters
        self.CenterClusterList = makeCenterClusterList(self.vectors_3dim, k, self.sc)
        self.arrow_size = arrow_size

    def find_elbow(self):
        mms = MinMaxScaler()
        mms.fit(self.vectors_3dim)
        data_transformed = mms.transform(self.vectors_3dim)

        Sum_of_squared_distances = []
        K = range(17, int(0.0031 * len(data_transformed)))
        for i, k in enumerate(K):
            sc = SpectralClusteringAlgorithm(n_clusters=k)
            sc = sc.fit(self.vectors_3dim)
            Sum_of_squared_distances.append(generateInteria_(self.vectors_3dim, k, sc))
            if (len(Sum_of_squared_distances)) > 2:
                gradient1 = Sum_of_squared_distances[i] - Sum_of_squared_distances[i - 1]
                gradient2 = Sum_of_squared_distances[i] - Sum_of_squared_distances[i - 2]
                if (gradient1 > -300) and (gradient2 > -300):
                    return k - 3

        # plt.plot(K, Sum_of_squared_distances, 'bx-')
        # plt.xlabel('k')
        # plt.ylabel('Sum_of_squared_distances')
        # plt.title('Elbow Method For Optimal k')
        # plt.show()
        # for i in range(2, len(Sum_of_squared_distances)):
        #     gradient1 = Sum_of_squared_distances[i] - Sum_of_squared_distances[i - 1]
        #     gradient2 = Sum_of_squared_distances[i] - Sum_of_squared_distances[i - 2]
        #     if (gradient1 > -300) and (gradient2 > -300):
        #         print(i+15)
        #         return i+15
        return 20

    def getPlot(self):
        # Create a scatter plot
        fig = plt.figure(dpi=120, figsize=(8.0, 5.0))
        ax = fig.add_subplot(projection='3d')

        #drow all the nodes in the grapg
        ax.scatter(self.vectors_3dim[:, 0], self.vectors_3dim[:, 1], self.vectors_3dim[:, 2], s=1, alpha=0.1)

        # drow the clusters and labels
        for name, vector in self.clustersNames().items():
            # clusters
            ax.scatter(vector[0],vector[1],vector[2], c=self.color, marker='^', s=600,depthshade=False, alpha=0.7)

            # labels
            ax.text(vector[0] - 0.3, vector[1] - 0.3, vector[2] - 0.3, name, None)

            # # drow clusters label
            # x2, y2, _ = proj3d.proj_transform(center[0],center[1],center[2], ax.get_proj())
            #
            # label = pylab.annotate(
            #     "S"+str(i),
            #     xy=(x2, y2), xytext=(self.arrow_size*1.4, self.arrow_size*0.6),
            #     textcoords='offset points', ha='right', va='bottom',
            #     bbox=dict(boxstyle='round,pad=0.5', fc=self.color, alpha=0.5),
            #     arrowprops=dict(arrowstyle='->', connectionstyle='arc3,rad=0'))
            #
            # def update_position(e):
            #     x2, y2, _ = proj3d.proj_transform(1, 1, 1, ax.get_proj())
            #     label.xy = x2, y2
            #     label.update_positions(fig.canvas.renderer)
            #     fig.canvas.draw()
            #
            # fig.canvas.mpl_connect('button_release_event', update_position)

        #the axis labels
        ax.set_xlabel('X Label')
        ax.set_ylabel('Y Label')
        ax.set_zlabel('Z Label')

        return pylab

    # Get dictionary of centers by cluster name
    def clustersNames(self):
        spectral_centers_name = {}
        for i, center in enumerate(self.CenterClusterList):
            spectral_centers_name["S" + str(i)] = center
        return spectral_centers_name