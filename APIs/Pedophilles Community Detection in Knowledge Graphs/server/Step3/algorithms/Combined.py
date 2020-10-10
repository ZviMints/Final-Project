import matplotlib as matplotlib
from matplotlib import pylab
from mpl_toolkits.mplot3d import proj3d
from sklearn.cluster import KMeans as KMeansAlgorithm  # Algorithm
import matplotlib.pyplot as plt
from sklearn.cluster import SpectralClustering as SpectralClusteringAlgorithm  # Algorithm
from sklearn.preprocessing import MinMaxScaler


# matplotlib.use('MacOSX')


class Combined:
    def __init__(self, kmeans, spectral, connected):
        self.kmeans = kmeans
        self.spectral = spectral
        self.connected = connected

    def kmeansPlot(self, ax, fig):
        # drow the clusters and labels
        for name, vector in self.kmeans.clustersNames().items():
            #clusters
            ax.scatter(vector[0], vector[1], vector[2],
                       s=750, c=self.kmeans.color, marker='o', depthshade=False, alpha=0.3)
            #labels
            ax.text(vector[0] - 0.3, vector[1] - 0.3, vector[2] - 0.3, name, None)

    def spectralPlot(self, ax, fig):
        # drow the clusters and labels
        for name, vector in self.spectral.clustersNames().items():
            # clusters
            ax.scatter(vector[0], vector[1], vector[2], c=self.spectral.color, marker='^', s=750, depthshade=False, alpha=0.5)

            # labels
            ax.text(vector[0] - 0.3, vector[1] - 0.3, vector[2] - 0.3, name, None)


    def connectedPlot(self, ax, fig):
        # drow the clusters and labels
        for name, vector in self.connected.clustersNames().items():
            #clusters
            ax.scatter(vector[0], vector[1], vector[2],
                       s=700, c=self.connected.color, marker='s', depthshade=False, alpha=0.2)
            #labels
            ax.text(vector[0] - 0.3, vector[1] - 0.3, vector[2] - 0.3, name, None)


    def getPlot(self, mode):
        # Create a scatter plot
        fig = plt.figure(dpi=120, figsize=(8.0, 5.0))
        ax = fig.add_subplot(projection='3d')

        # # drow all the nodes in the graph
        # ax.scatter(self.kmeans.vectors_3dim[:, 0], self.kmeans.vectors_3dim[:, 1], self.kmeans.vectors_3dim[:, 2],
        #            s=1, alpha=0.1)

        if mode == "kmeans+spectral":
            # drow kmeans clusters
            self.kmeansPlot(ax, fig)
            # drow spectral clusters
            self.spectralPlot(ax, fig)

        elif mode == "kmeans+connected":
            # drow kmeans clusters
            self.kmeansPlot(ax, fig)
            # drow connected clusters
            self.connectedPlot(ax, fig)

        elif mode == "spectral+connected":
            # drow spectral clusters
            self.spectralPlot(ax, fig)
            # drow connected clusters
            self.connectedPlot(ax, fig)

        elif mode == "kmeans+spectral+connected":
            # drow kmeans clusters
            self.kmeansPlot(ax, fig)
            # drow spectral clusters
            self.spectralPlot(ax, fig)
            # drow connected clusters
            self.connectedPlot(ax, fig)

            # the axis labels
            ax.set_xlabel('X Label')
            ax.set_ylabel('Y Label')
            ax.set_zlabel('Z Label')
        return pylab
