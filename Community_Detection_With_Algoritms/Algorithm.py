import matplotlib as matplotlib
from .algorithms import KMeans
from .algorithms import ConnectedComponents
from .algorithms import SpectralClustering

class Algorithm:
    def __init__(self, figure, vectors_3dim):
        self.kmeans = KMeans(self.vectors_3dim, self.figure)
        self.cc = ConnectedComponents(self.vectors_3dim, self.figure)
        self.spectral = SpectralClustering(self.vectors_3dim, self.figure)

matplotlib.use('MacOSX')



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

