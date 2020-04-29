import matplotlib as matplotlib
from .algorithms import KMeans
from .algorithms import ConnectedComponents
from .algorithms import SpectralClustering
matplotlib.use('MacOSX')

class Algorithm:
    def __init__(self, base_figure, vectors_3dim):
        self.kmeans = KMeans(vectors_3dim, base_figure)
        self.cc = ConnectedComponents(vectors_3dim, base_figure)
        self.spectral = SpectralClustering(vectors_3dim, base_figure)


    # Plotting the Graph with KMeans
    def kmeansPlot(self):
        self.kmeans.run().show()

    # Plotting the Graph with ConnectedComponents
    def ccPlot(self):
        self.cc.run().show()

    # Plotting the Graph with SpectralClustering
    def spectralPlot(self):
        self.cc.run().show()

    def combinedPlot(self):
        ()

