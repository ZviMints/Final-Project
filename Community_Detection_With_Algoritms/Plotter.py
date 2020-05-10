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

# =============================================== Help Methods ===============================================
def union_to_one_componenet(sets_3dim_vecs):
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


def make_PCA(G, model):
    sets_of_64dim = get_connect_nodes_by_64dim(G, model)
    return get_3dim_sets_from_64dim(sets_of_64dim)


# =============================================== Plotter ===============================================
# This class is responsible to plot
# He has algorithms and functions
class Plotter:

    # G is networkx
    # model is after node2vec embedded
    def __init__(self, G, model):
        all_connected_componenets_after_pca = make_PCA(G, model)

        one_componenet_after_pca = union_to_one_componenet(all_connected_componenets_after_pca)

        self.make_df(one_componenet_after_pca)

        # Make base graph (without algorithm)
        self.BaseGraph = BaseGraph.BaseGraph(one_componenet_after_pca, self.df)

        # Make Kmeans
        self.kmeans = KMeans.KMeans(one_componenet_after_pca, self.df, "red")

        # Make Connected Componenet
        self.cc = ConnectedComponents.ConnectedComponents(all_connected_componenets_after_pca, self.df, "green")

        # Make Spectral
        self.spectral = SpectralClustering.SpectralClustering(one_componenet_after_pca, self.df, "yellow")

    def make_df(self,one_componenet_after_pca):
        self.df = pd.DataFrame(one_componenet_after_pca)  # 2-dimensional labeled data structure with columns of potentially different types

        self.df['pca-one'] = one_componenet_after_pca[:, 0]
        self.df['pca-two'] = one_componenet_after_pca[:, 1]
        self.df['pca-three'] = one_componenet_after_pca[:, 2]

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

    def showCombined(self): #todo: eilon
        ()
