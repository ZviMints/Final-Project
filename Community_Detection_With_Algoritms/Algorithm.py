import matplotlib as matplotlib
from .algorithms import KMeans
from .algorithms import ConnectedComponents
from .algorithms import SpectralClustering
from .algorithms import Undefined
matplotlib.use('MacOSX')

class Algorithm:
    def __init__(self, figure, vectors_3dim, algorithm):
        self.vectors_3dim = vectors_3dim
        self.figure = figure

        switcher = {
            "k-means": KMeans(self.vectors_3dim, self.figure),
            "connected-componenets": ConnectedComponents(self.vectors_3dim, self.figure),
            "spectral-clustering": SpectralClustering(self.vectors_3dim, self.figure),
        }
        self.algorithm = switcher.get(algorithm, Undefined())


    # Plotting the Graph
    def show(self):
            self.algorithm.run().show()
