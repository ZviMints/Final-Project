import matplotlib as matplotlib
from sklearn.cluster import KMeans as KMeansAlgorithm # Algorithm
from sklearn.cluster import SpectralClustering as SpectralClusteringAlgorithm # Algorithm
import matplotlib.pyplot as plt
import pandas as pd
# matplotlib.use('MacOSX')

class cluster_Kmean:
    def __init__(self, vectors_3dim, color):
        self.vectors_3dim = vectors_3dim
        self.color = color

    def getPlot(self):
        df = pd.DataFrame(
            self.vectors_3dim)  # 2-dimensional labeled data structure with columns of potentially different types

        df['pca-one'] = self.vectors_3dim[:, 0]
        df['pca-two'] = self.vectors_3dim[:, 1]
        df['pca-three'] = self.vectors_3dim[:, 2]

        # Create a scatter plot for k-means
        base_figure = plt.figure(dpi=50, figsize=(160, 100)).gca(projection='3d')
        base_figure.scatter(
            xs=df["pca-one"],
            ys=df["pca-two"],
            zs=df["pca-three"],
            cmap='red'
        )



        km = KMeansAlgorithm(n_clusters=4, init='k-means++', max_iter=300, n_init=10, random_state=0)
        km.fit_predict(self.vectors_3dim)
        base_figure.scatter(km.cluster_centers_[:, 0], km.cluster_centers_[:, 1], km.cluster_centers_[:, 2], s=10000,c=self.color)


        sc = SpectralClusteringAlgorithm(n_clusters=4, affinity='nearest_neighbors')
        labels = sc.fit_predict(self.vectors_3dim)
        base_figure.scatter(self.vectors_3dim[:, 0], self.vectors_3dim[:, 1], self.vectors_3dim[:, 2], s=50,
                                    c=labels)

        # base_figure.set_xlabel('pca-one')
        # base_figure.set_ylabel('pca-two')
        # base_figure.set_zlabel('pca-three')
        return plt

