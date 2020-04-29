import matplotlib as matplotlib
from . import algorithms
matplotlib.use('MacOSX')

class Algorithm:
    def __init__(self, figure, vectors_3dim, algorithm):
        self.vectors_3dim = vectors_3dim
        self.figure = figure
        self.algorithm = algorithm

    # Getting the write algorithm
    def getPlot(self):
        switcher = {
            "k-means": algorithms.KMeans(self.vectors_3dim,self.figure).run(),
            "connected-componenets": algorithms.ConnectedComponents(self.vectors_3dim,self.figure).run(),
            "spectral-clustering": algorithms.SpectralClustering(self.vectors_3dim,self.figure).run()
        }
        return switcher.get(self.algorithm, None)


    # Plotting the Graph
    def show(self):
        plt =  self.getPlot()
        if(plt == None):
            raise RuntimeError('There no such algorithm!')
        else:
            plt.show()
