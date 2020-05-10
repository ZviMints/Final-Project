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

def main():
    # ======================================== Getting (G,model) ======================================== #
    # Taking G from memory
    G = nx.read_multiline_adjlist("adjlists/test_networkxAfterRemove.adjlist")

    # Taking Memory from memory
    fname = "test_embedded_vectors_model.kv"
    path = get_tmpfile(fname)
    model = KeyedVectors.load(path, mmap='r')

    # ======================================== Plotting ======================================== #
    plt = Plotter.Plotter(G, model)

    plt.showWithNoAlgo()
    plt.showWithKMeans()
    plt.showWithCC()
    plt.showWithSpectral()

if __name__ == '__main__':
    main()
