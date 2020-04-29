import matplotlib as matplotlib
from sklearn.cluster import SpectralClustering as SpectralClusteringAlgorithm # Algorithm
import matplotlib.pyplot as plt
import pandas as pd
# matplotlib.use('MacOSX')

class SpectralClustering:
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

        sc = SpectralClusteringAlgorithm(n_clusters=4, affinity='nearest_neighbors')
        labels = sc.fit_predict(self.vectors_3dim)
        base_figure.scatter(self.vectors_3dim[:,0] , self.vectors_3dim[:, 1], self.vectors_3dim[:, 2], s=50,c=labels)
        base_figure.set_xlabel('pca-one')
        base_figure.set_ylabel('pca-two')
        base_figure.set_zlabel('pca-three')
        return plt
