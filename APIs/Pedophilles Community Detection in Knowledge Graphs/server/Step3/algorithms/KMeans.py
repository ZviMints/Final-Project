import matplotlib as matplotlib
from matplotlib import pylab
from mpl_toolkits.mplot3d import proj3d
from sklearn.cluster import KMeans as KMeansAlgorithm  # Algorithm
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
from matplotlib import cm

MAX_CLUSTERS_ANOUNT = 10
# matplotlib.use('MacOSX')

class KMeans:
    def __init__(self, vectors_3dim, color, arrow_size):
        self.vectors_3dim = vectors_3dim
        self.color = color
        self.km = KMeansAlgorithm(n_clusters=self.find_elbow(), init='k-means++', max_iter=300, n_init=10,
                                  random_state=0)
        self.km.fit_predict(self.vectors_3dim)
        self.arrow_size = arrow_size

    def find_elbow(self):
        mms = MinMaxScaler()
        mms.fit(self.vectors_3dim)
        data_transformed = mms.transform(self.vectors_3dim)

        Sum_of_squared_distances = []
        K = range(1, int(0.01 * len(data_transformed)))
        for k in K:
            km = KMeansAlgorithm(n_clusters=k)
            km = km.fit(self.vectors_3dim)
            Sum_of_squared_distances.append(km.inertia_)
            if (len(Sum_of_squared_distances)) > 1:
                gradient = Sum_of_squared_distances[k - 1] - Sum_of_squared_distances[k - 2]
                if gradient > -1200:
                    return k - 3

    def getPlot(self):

        # Create a scatter plot
        fig = plt.figure(dpi=120, figsize=(8.0, 5.0))
        ax = fig.add_subplot(111, projection='3d')

        # drow all the nodes in the graph
        ax.scatter(self.vectors_3dim[:, 0], self.vectors_3dim[:, 1], self.vectors_3dim[:, 2], s=1, alpha=0.1)

        # drow the clusters and labels
        for name, vector in self.clustersNames().items():
            #clusters
            ax.scatter(vector[0], vector[1], vector[2],
                       s=750, c=self.color, marker='o', depthshade=False, alpha=0.3)
            #labels
            ax.text(vector[0] - 0.3, vector[1] - 0.3, vector[2] - 0.3, name, None)


        # the axis labels
        ax.set_xlabel('X Label')
        ax.set_ylabel('Y Label')
        ax.set_zlabel('Z Label')
        return pylab


    # Get dictionary of centers by cluster name
    def clustersNames(self):
        kmeans_centers_name = {}
        for i, center in enumerate(self.km.cluster_centers_):
            if i < MAX_CLUSTERS_ANOUNT:
                kmeans_centers_name["K" + str(i)] = center
        return kmeans_centers_name

