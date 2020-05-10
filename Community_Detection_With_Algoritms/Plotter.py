import matplotlib as matplotlib
import networkx as nx
import numpy as np
import pandas as pd
from sklearn import decomposition
from sklearn.preprocessing import StandardScaler
from Community_Detection_With_Algoritms.algorithms import KMeans
from Community_Detection_With_Algoritms.algorithms import BaseGraph
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

def get_connect_nodes_by_64dim(G, model):
    connected_nodes_sets_64dim = []
    connected_nodes_by_id = list(nx.connected_components(G))
    for group in connected_nodes_by_id:
        set_of_64dim_vectors = []
        for node_id in group:
            set_of_64dim_vectors.append(model.get_vector(node_id))

        connected_nodes_sets_64dim.append(set_of_64dim_vectors)
    return connected_nodes_sets_64dim


def get_3dim_sets_from_64dim(connected_nodes_sets_64dim):
    sets_of_3dim = []
    # PCA Algorithm
    pca = decomposition.PCA(n_components=3)
    scaler =StandardScaler()#Normalizer(norm='max')
    for set_of_64dim in connected_nodes_sets_64dim:
        vectors64_scale = scaler.fit_transform(set_of_64dim)
        sets_of_3dim.append(pca.fit_transform(vectors64_scale))
    return sets_of_3dim


def make_sets_3dim_vec(G, model):
    sets_of_64dim = get_connect_nodes_by_64dim(G, model)
    return get_3dim_sets_from_64dim(sets_of_64dim)

class Plotter:
    def __init__(self, G, model):
        sets_vectors_3dim = make_sets_3dim_vec(G, model)
        union_vecs = union(sets_vectors_3dim)
        self.make_df(union_vecs)
        self.BaseGraph = BaseGraph.BaseGraph(union_vecs, self.df)
        self.kmeans = KMeans.KMeans(union_vecs, self.df, "red")
        self.cc = ConnectedComponents.ConnectedComponents(sets_vectors_3dim, self.df, "green")
        self.spectral = SpectralClustering.SpectralClustering(union_vecs, self.df, "yellow")

    def make_df(self,union_vecs):
        self.df = pd.DataFrame(
            union_vecs)  # 2-dimensional labeled data structure with columns of potentially different types

        self.df['pca-one'] = union_vecs[:, 0]
        self.df['pca-two'] = union_vecs[:, 1]
        self.df['pca-three'] = union_vecs[:, 2]

    # Plotting the Graph with no algo
    def showWithNoAlgo(self):
        self.BaseGraph.getPlot().show()

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
