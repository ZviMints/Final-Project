import matplotlib as matplotlib
from sklearn.cluster import KMeans as KMeansAlgorithm # Algorithm
import matplotlib.pyplot as plt
import pandas as pd
matplotlib.use('MacOSX')

class KMeans:
    def __init__(self, vectors_3dim):
        self.vectors_3dim = vectors_3dim

    def getPlot(self):
        df = pd.DataFrame(
            self.vectors_3dim)  # 2-dimensional labeled data structure with columns of potentially different types

        df['pca-one'] = self.vectors_3dim[:, 0]
        df['pca-two'] = self.vectors_3dim[:, 1]
        df['pca-three'] = self.vectors_3dim[:, 2]

        # Create a scatter plot
        base_figure = plt.figure(dpi=50, figsize=(160, 100)).gca(projection='3d')
        base_figure.scatter(
            xs=df["pca-one"],
            ys=df["pca-two"],
            zs=df["pca-three"],
            cmap='red'
        )

        km = KMeansAlgorithm(n_clusters=4, init='k-means++', max_iter=300, n_init=10, random_state=0)
        km.fit_predict(self.vectors_3dim)
        base_figure.scatter(km.cluster_centers_[:, 0], km.cluster_centers_[:, 1], km.cluster_centers_[:, 2], s=10000,
                            c='red')
        base_figure.set_xlabel('pca-one')
        base_figure.set_ylabel('pca-two')
        base_figure.set_zlabel('pca-three')
        return plt

