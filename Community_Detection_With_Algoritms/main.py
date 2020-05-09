import networkx as nx
from gensim.models import KeyedVectors
import numpy as np
from sklearn import decomposition

from Community_Detection_With_Algoritms import Plotter
from gensim.test.utils import get_tmpfile
from sklearn.decomposition import PCA  # From 64dim to 3dim
from sklearn.preprocessing import StandardScaler

import matplotlib.pyplot

# matplotlib.use('MacOSX')
# Zvi Mints and Eilon Tsadok - Mac Version

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
    # pca = PCA(n_components=3)
    pca = decomposition.PCA(n_components=3)
    scaler =StandardScaler()#Normalizer(norm='max')
    for set_of_64dim in connected_nodes_sets_64dim:
        vectors64_scale = scaler.fit_transform(set_of_64dim)
        sets_of_3dim.append(pca.fit_transform(vectors64_scale))

    return sets_of_3dim


def make_sets_3dim_vec(G, model):
    sets_of_64dim = get_connect_nodes_by_64dim(G, model)
    return get_3dim_sets_from_64dim(sets_of_64dim)



G = nx.read_multiline_adjlist("test_networkxAfterRemove.adjlist")

fname = "test_embedded_vectors_model.kv"
path = get_tmpfile(fname)
model = KeyedVectors.load(path, mmap='r')



sets_vectors_3dim = make_sets_3dim_vec(G, model)

# Plot the Algorithm
plt = Plotter.Plotter(sets_vectors_3dim)
# plt.showWithNoAlgo()
# plt.showWithKMeans()
# plt.showWithCC()
plt.showWithSpectral()


