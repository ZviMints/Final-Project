# Taking G from memory
import math
import numpy as np
import networkx
from gensim.models import KeyedVectors
from gensim.test.utils import get_tmpfile

from BERT.clustersBy3DVec import clustersBy3DVec
from Community_Detection_With_Algoritms import Plotter


G = networkx.read_multiline_adjlist("./adjlists/graph.adjlist")
# Taking Memory from memory
fname = "model.kv"
path = get_tmpfile(fname)
model = KeyedVectors.load(path, mmap='r')


#get centers with name of all
plotter = Plotter.Plotter(G, model)
(kmeans_centers,spectral_centers,connected_center) = plotter.getAllCentersName()
clusters = clustersBy3DVec(kmeans_centers,spectral_centers,connected_center,plotter.all_vectors_after_pca)




