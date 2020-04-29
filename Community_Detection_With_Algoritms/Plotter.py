import matplotlib as matplotlib
import algorithms

matplotlib.use('MacOSX')


class Plotter:
    def __init__(self, vectors_3dim):
        self.kmeans = algorithms.KMeans(vectors_3dim, "red")
        self.cc = algorithms.ConnectedComponents(vectors_3dim, "yellow")
        self.spectral = algorithms.SpectralClustering(vectors_3dim, "blue")

    # Plotting the Graph with KMeans
    def showWithKMeans(self):
        self.kmeans.getPlot().show()

    # Plotting the Graph with ConnectedComponents
    def showWithCC(self):
        self.cc.getPlot().show()

    # Plotting the Graph with SpectralClustering
    def showWithSpectral(self):
        self.spectral.getPlot().show()

    def showCombined(self):
        ()
