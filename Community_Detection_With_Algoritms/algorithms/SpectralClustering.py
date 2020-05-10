from datetime import datetime
import time
from sklearn.cluster import SpectralClustering as SpectralClusteringAlgorithm # Algorithm
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.preprocessing import MinMaxScaler

# matplotlib.use('MacOSX')

class SpectralClustering:
    def __init__(self, vectors_3dim, df, color):
        self.vectors_3dim = vectors_3dim
        self.df = df
        self.color = color

    def find_elbow(self):
        mms = MinMaxScaler()
        mms.fit(self.vectors_3dim)
        data_transformed = mms.transform(self.vectors_3dim)

        Sum_of_squared_distances = []
        K = range(1, int(0.01 * len(data_transformed)))
        for k in K:
            sc = SpectralClusteringAlgorithm(n_clusters=k)
            sc = sc.fit(self.vectors_3dim)
            # Sum_of_squared_distances.append(sc.inertia_)
            # if (len(Sum_of_squared_distances)) > 1:
            #     gradient = Sum_of_squared_distances[k - 1] - Sum_of_squared_distances[k - 2]
            #     if gradient > -1000:
            #         return k - 1
        plt.plot(K, Sum_of_squared_distances, 'bx-')
        plt.xlabel('k')
        plt.ylabel('Sum_of_squared_distances')
        plt.title('Elbow Method For Optimal k')
        plt.show()

    def getPlot(self):

        # Create a scatter plot
        base_figure = plt.figure(dpi=120, figsize=(160, 100)).gca(projection='3d')
        base_figure.scatter(
            xs=self.df["pca-one"],
            ys=self.df["pca-two"],
            zs=self.df["pca-three"],
            s=1
        )

        sc = SpectralClusteringAlgorithm(n_clusters=11, assign_labels="discretize",n_init=10, random_state=0)
        sc.fit_predict(self.vectors_3dim)
        base_figure.scatter(sc.affinity_matrix_[:,0] , sc.affinity_matrix_[:, 1], sc.affinity_matrix_[:, 2], s=1000,c=self.color, depthshade=False)

        base_figure.set_xlabel('x axis')
        base_figure.set_ylabel('y axis')
        base_figure.set_zlabel('z axis')
        return plt
