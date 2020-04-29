import matplotlib as matplotlib
from sklearn.cluster import KMeans # Algorithm
# matplotlib.use('MacOSX')

class KMeans:
    def __init__(self, figure, vectors_3dim):
        self.vectors_3dim = vectors_3dim
        self.figure = figure


    def run(self):
        km = KMeans(n_clusters=4, init='k-means++', max_iter=300, n_init=10, random_state=0)
        km.fit_predict(self.vectors_3dim)
        self.figure.scatter(km.cluster_centers_[:, 0], km.cluster_centers_[:, 1], km.cluster_centers_[:, 2], s=10000,c='red')
        self.figure.set_xlabel('pca-one')
        self.figure.set_ylabel('pca-two')
        self.figure.set_zlabel('pca-three')
        return self.figure

