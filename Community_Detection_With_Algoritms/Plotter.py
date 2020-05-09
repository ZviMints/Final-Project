import matplotlib as matplotlib
import numpy as np
import pandas as pd

from Community_Detection_With_Algoritms.algorithms import KMeans
from Community_Detection_With_Algoritms.algorithms import No_Algo
from Community_Detection_With_Algoritms.algorithms import ConnectedComponents
from Community_Detection_With_Algoritms.algorithms import SpectralClustering
import matplotlib.pyplot as plt

# matplotlib.use('MacOSX')

def union(sets_3dim_vecs):
    # for set in sets_3dim_vecs:
    union_3dim = list()
    for nodes_set in sets_3dim_vecs:
        for node in nodes_set:
            union_3dim.append([node[0], node[1], node[2]])
    union_3dim = np.array(union_3dim)
    return union_3dim





class Plotter:
    def __init__(self, sets_vectors_3dim):
        self.union_vecs = union(sets_vectors_3dim)
        self.make_df()
        self.NoAlgo = No_Algo.No_Algo(self.union_vecs,self.df)
        self.kmeans = KMeans.KMeans(self.union_vecs, self.df, "red")
        self.cc = ConnectedComponents.ConnectedComponents(sets_vectors_3dim, self.df, "green")
        self.spectral = SpectralClustering.SpectralClustering(self.union_vecs,self.df, "yellow")


    def make_df(self):
        self.df = pd.DataFrame(
            self.union_vecs)  # 2-dimensional labeled data structure with columns of potentially different types

        self.df['pca-one'] = self.union_vecs[:, 0]
        self.df['pca-two'] = self.union_vecs[:, 1]
        self.df['pca-three'] = self.union_vecs[:, 2]

    # Plotting the Graph with no algo
    def showWithNoAlgo(self):
        self.NoAlgo.getPlot().show()

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
