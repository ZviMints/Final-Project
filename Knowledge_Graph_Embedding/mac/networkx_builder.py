import networkx as nx
import matplotlib as matplotlib
from node2vec import Node2Vec

matplotlib.use('MacOSX')

# Zvi Mints and Eilon Tsadok - Mac Version
G = nx.read_multiline_adjlist("convesations.adjlist")


# Part A
"""
     :param G: Input graph
     :param dimensions: Embedding dimensions
     :param walk_length: Number of nodes in each walk
     :param num_walks: Number of walks per node
     :param workers: Number of workers for parallel execution
"""

node2vec = Node2Vec(G, dimensions=64, walk_length=30, num_walks=200, workers=1)  # Use temp_folder for big graphs
print(node2vec.walks)
