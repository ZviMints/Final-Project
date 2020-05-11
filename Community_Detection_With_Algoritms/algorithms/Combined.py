import matplotlib as matplotlib
from sklearn.cluster import KMeans as KMeansAlgorithm # Algorithm
import matplotlib.pyplot as plt
from sklearn.cluster import SpectralClustering as SpectralClusteringAlgorithm # Algorithm
from sklearn.preprocessing import MinMaxScaler

# matplotlib.use('MacOSX')


class Combined:
    def __init__(self, df,kmeans,spectral,connected):
        self.df = df
        self.kmeans = kmeans
        self.spectral =spectral
        self.connected = connected


    def getPlot(self, mode):
        # Create a scatter plot
        base_figure = plt.figure(dpi=120, figsize=(8.0, 5.0)).gca(projection='3d')
        base_figure.scatter(
            xs=self.df["pca-one"],
            ys=self.df["pca-two"],
            zs=self.df["pca-three"],
            s=1)

        if mode == "kmeans+spectral":
            base_figure.scatter(self.kmeans.km.cluster_centers_[:, 0], self.kmeans.km.cluster_centers_[:, 1],
                                self.kmeans.km.cluster_centers_[:, 2], s=700, c=self.kmeans.color, depthshade=False)
            base_figure.scatter(self.spectral.vectors_3dim[:,0] , self.spectral.vectors_3dim[:, 1], self.spectral.vectors_3dim[:, 2],
                                s=1,c=self.spectral.sc.labels_, depthshade=False)
        elif mode == "kmeans+connected":
            base_figure.scatter(self.kmeans.km.cluster_centers_[:, 0], self.kmeans.km.cluster_centers_[:, 1],
                                self.kmeans.km.cluster_centers_[:, 2], s=700, c=self.kmeans.color, depthshade=False)
            base_figure.scatter(
                xs=self.connected.component_centers[:, 0],
                ys=self.connected.component_centers[:, 1],
                zs=self.connected.component_centers[:, 2],
                depthshade=False,
                s=self.connected.component_radiuses,
                c=self.connected.color
            )

        elif mode == "spectral+connected":
            base_figure.scatter(self.spectral.vectors_3dim[:, 0], self.spectral.vectors_3dim[:, 1],
                                self.spectral.vectors_3dim[:, 2],
                                s=1, c=self.spectral.sc.labels_, depthshade=False)
            base_figure.scatter(
                xs=self.connected.component_centers[:, 0],
                ys=self.connected.component_centers[:, 1],
                zs=self.connected.component_centers[:, 2],
                depthshade=False,
                s=self.connected.component_radiuses,
                c=self.connected.color)

        elif mode == "kmeans+spectral+connected":
            base_figure.scatter(self.kmeans.km.cluster_centers_[:, 0], self.kmeans.km.cluster_centers_[:, 1],
                                self.kmeans.km.cluster_centers_[:, 2], s=700, c=self.kmeans.color, depthshade=False)
            base_figure.scatter(self.spectral.vectors_3dim[:, 0], self.spectral.vectors_3dim[:, 1],
                                self.spectral.vectors_3dim[:, 2],
                                s=1, c=self.spectral.sc.labels_, depthshade=False)
            base_figure.scatter(
                xs=self.connected.component_centers[:, 0],
                ys=self.connected.component_centers[:, 1],
                zs=self.connected.component_centers[:, 2],
                depthshade=False,
                s=self.connected.component_radiuses,
                c=self.connected.color)


        base_figure.set_xlabel('x axis')
        base_figure.set_ylabel('y axis')
        base_figure.set_zlabel('z axis')
        return plt

