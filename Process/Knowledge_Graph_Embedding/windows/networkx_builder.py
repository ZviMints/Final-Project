import networkx as nx
import matplotlib as matplotlib
from node2vec import Node2Vec
from gensim.test.utils import get_tmpfile
# matplotlib.use('MacOSX')

# Zvi Mints and Eilon Tsadok - Mac Version

def saveWalks(walks):
    f = open("walks_test.txt", "w+")
    row = 1
    for sentence in walks:
        f.write("row %s:    " % str(row))
        row = row + 1
        for word in sentence:
            f.write(word)
            f.write("  ")
        f.write("\n")
    f.close()

# Start Point:
G = nx.read_multiline_adjlist("test_networkxAfterRemove.adjlist")


# Part A
"""
     :param G: Input graph
     :param dimensions: Embedding dimensions
     :param walk_length: Number of nodes in each walk
     :param num_walks: Number of walks per node
     :param workers: Number of workers for parallel execution
"""

# Precompute probabilities and generate walks
node2vec = Node2Vec(G, dimensions=64, walk_length=25, num_walks=10, workers=1)

saveWalks(list(node2vec.walks))

# Embed nodes
model = node2vec.fit(window=10, min_count=1, batch_words=4)

# Look for most similar nodes
for node, enc in model.wv.most_similar('f139aba52f9fa1394b4034a7954b2220'):  # Output node names are always strings
    print(node, enc)

# Print the 64dim of vector
print("64dim vector representation for `f139aba52f9fa1394b4034a7954b2220`: ")
print(model.wv.get_vector('f139aba52f9fa1394b4034a7954b2220'))

# Save the model into
fname = "test_embedded_vectors_model.kv"
path = get_tmpfile(fname)
model.wv.save(path)
print("file %s saved" % fname)