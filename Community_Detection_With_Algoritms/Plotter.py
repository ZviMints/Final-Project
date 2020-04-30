import matplotlib as matplotlib
from sklearn.preprocessing import MinMaxScaler

from Community_Detection_With_Algoritms.algorithms import KMeans
from Community_Detection_With_Algoritms.algorithms import ConnectedComponents
from Community_Detection_With_Algoritms.algorithms import SpectralClustering
from sklearn.cluster import KMeans as KMeansAlgorithm # Algorithm
import matplotlib.pyplot as plt

matplotlib.use('MacOSX')


class Plotter:
    def __init__(self, vectors_3dim):
        self.vectors_3dim = vectors_3dim
        self.kmeans = KMeans.KMeans(vectors_3dim, "red")
        self.cc = ConnectedComponents.ConnectedComponents(vectors_3dim, "yellow")
        self.spectral = SpectralClustering.SpectralClustering(vectors_3dim)



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
