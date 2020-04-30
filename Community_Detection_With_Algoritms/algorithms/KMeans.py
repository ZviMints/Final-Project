import matplotlib as matplotlib
from sklearn.cluster import KMeans as KMeansAlgorithm # Algorithm
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.cluster import SpectralClustering as SpectralClusteringAlgorithm # Algorithm
from sklearn.preprocessing import MinMaxScaler

matplotlib.use('MacOSX')


class KMeans:
    def __init__(self, vectors_3dim, color):
        self.vectors_3dim = vectors_3dim
        self.color = color

    def find_elbow(self):
        mms = MinMaxScaler()
        mms.fit(self.vectors_3dim)
        data_transformed = mms.transform(self.vectors_3dim)

        Sum_of_squared_distances = []
        K = range(1, int(0.01*len(data_transformed)))
        for k in K:
            km = KMeansAlgorithm(n_clusters=k)
            km = km.fit(self.vectors_3dim)
            Sum_of_squared_distances.append(km.inertia_)
            if (len(Sum_of_squared_distances))>1:
                gradient= Sum_of_squared_distances[k-1]-Sum_of_squared_distances[k-2]
                if gradient>-1000:
                    return k-1
        # plt.plot(K, Sum_of_squared_distances, 'bx-')
        # plt.xlabel('k')
        # plt.ylabel('Sum_of_squared_distances')
        # plt.title('Elbow Method For Optimal k')
        # plt.show()


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



        km = KMeansAlgorithm(n_clusters=self.find_elbow(), init='k-means++', max_iter=300, n_init=10, random_state=0)
        km.fit_predict(self.vectors_3dim)
        base_figure.scatter(km.cluster_centers_[:, 0], km.cluster_centers_[:, 1], km.cluster_centers_[:, 2], s=7000,c=self.color)


        base_figure.set_xlabel('pca-one')
        base_figure.set_ylabel('pca-two')
        base_figure.set_zlabel('pca-three')
        return plt

