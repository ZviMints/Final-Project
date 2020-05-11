import matplotlib as matplotlib
from sklearn.cluster import KMeans as KMeansAlgorithm # Algorithm
import matplotlib.pyplot as plt
from sklearn.cluster import SpectralClustering as SpectralClusteringAlgorithm # Algorithm
from sklearn.preprocessing import MinMaxScaler

# matplotlib.use('MacOSX')


class Combined:
    def __init__(self, kmeans,spectral,connected):
        self.kmeans = kmeans
        self.spectral =spectral
        self.connected = connected


    def getPlot(self, mode):
        # Create a scatter plot
        fig = plt.figure(dpi=120, figsize=(8.0, 5.0))
        ax = fig.add_subplot( projection='3d')

        # drow all the nodes in the grapg
        ax.scatter(self.kmeans.vectors_3dim[:, 0], self.kmeans.vectors_3dim[:, 1], self.kmeans.vectors_3dim[:, 2], s=1)

        if mode == "kmeans+spectral":
            # drow kmeans clusters
            ax.scatter(self.kmeans.km.cluster_centers_[:, 0], self.kmeans.km.cluster_centers_[:, 1],
                       self.kmeans.km.cluster_centers_[:, 2], s=700, c=self.kmeans.color, marker='o', depthshade=False)
            # drow spectral clusters
            for i in range(len(self.spectral.CenterClusterList)):
                center = self.spectral.CenterClusterList[i]
                ax.scatter(center[0], center[1], center[2], c=self.spectral.color, marker='^', s=700, depthshade=False)

        elif mode == "kmeans+connected":
            # drow kmeans clusters
            ax.scatter(self.kmeans.km.cluster_centers_[:, 0], self.kmeans.km.cluster_centers_[:, 1],
                       self.kmeans.km.cluster_centers_[:, 2], s=700, c=self.kmeans.color, marker='o', depthshade=False)
            # drow connected clusters
            ax.scatter(
                xs=self.connected.component_centers[:, 0],
                ys=self.connected.component_centers[:, 1],
                zs=self.connected.component_centers[:, 2],
                s=self.connected.component_radiuses,
                c=self.connected.color,
                marker='s',
                depthshade=False)

        elif mode == "spectral+connected":
            # drow spectral clusters
            for i in range(len(self.spectral.CenterClusterList)):
                center = self.spectral.CenterClusterList[i]
                ax.scatter(center[0], center[1], center[2], c=self.spectral.color, marker='^', s=700, depthshade=False)
            # drow connected clusters
            ax.scatter(
                xs=self.connected.component_centers[:, 0],
                ys=self.connected.component_centers[:, 1],
                zs=self.connected.component_centers[:, 2],
                s=self.connected.component_radiuses,
                c=self.connected.color,
                marker='s',
                depthshade=False)

        elif mode == "kmeans+spectral+connected":
            # drow kmeans clusters
            ax.scatter(self.kmeans.km.cluster_centers_[:, 0], self.kmeans.km.cluster_centers_[:, 1],
                       self.kmeans.km.cluster_centers_[:, 2], s=700, c=self.kmeans.color, marker='o', depthshade=False)
            # drow spectral clusters
            for i in range(len(self.spectral.CenterClusterList)):
                center = self.spectral.CenterClusterList[i]
                ax.scatter(center[0], center[1], center[2], c=self.spectral.color, marker='^', s=700, depthshade=False)
            # drow connected clusters
            ax.scatter(
                xs=self.connected.component_centers[:, 0],
                ys=self.connected.component_centers[:, 1],
                zs=self.connected.component_centers[:, 2],
                s=self.connected.component_radiuses,
                c=self.connected.color,
                marker='s',
                depthshade=False)

            # the axis labels
            ax.set_xlabel('X Label')
            ax.set_ylabel('Y Label')
            ax.set_zlabel('Z Label')
        return plt

