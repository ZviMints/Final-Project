import matplotlib as matplotlib
from sklearn.cluster import KMeans as KMeansAlgorithm # Algorithm
import matplotlib.pyplot as plt
from sklearn.cluster import SpectralClustering as SpectralClusteringAlgorithm # Algorithm
from sklearn.preprocessing import MinMaxScaler

# matplotlib.use('MacOSX')


class BaseGraph:
    def __init__(self, vectors_3dim, df):
        self.vectors_3dim = vectors_3dim
        self.df = df

    def getPlot(self):
        # Create a scatter plot
        base_figure = plt.figure(dpi=120, figsize=(160, 100)).gca(projection='3d')
        base_figure.scatter(
            xs=self.df["pca-one"],
            ys=self.df["pca-two"],
            zs=self.df["pca-three"],
            s=1
        )
        base_figure.set_xlabel('x axis')
        base_figure.set_ylabel('y axis')
        base_figure.set_zlabel('z axis')
        return plt

