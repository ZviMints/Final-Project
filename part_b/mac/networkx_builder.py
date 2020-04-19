import networkx as nx
import ijson
import matplotlib as matplotlib
from matplotlib import pyplot as plt
import networkx as nx
from node2vec import Node2Vec

matplotlib.use('MacOSX')


# Zvi Mints and Eilon Tsadok - Mac Version
G = nx.read_multiline_adjlist("convesations.adjlist")

# Precompute probabilities and generate walks
node2vec = Node2Vec(G, dimensions=64, walk_length=30, num_walks=200, workers=4)  # Use temp_folder for big graphs

# Embed nodes
model = node2vec.fit(window=10, min_count=1, batch_words=4)

# Look for most similar nodes
for node,emb in model.wv.most_similar('74bfc043bd5ce9c17b37ffae6e0ba2fa'):
    print(node,emb)