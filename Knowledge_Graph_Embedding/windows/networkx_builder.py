import networkx as nx
import matplotlib as matplotlib
from node2vec import Node2Vec
from gensim.test.utils import get_tmpfile
from gensim.models import KeyedVectors

# Zvi Mints and Eilon Tsadok - Windows Version

def make_file_of_sampling_sentences():
    f = open("sampling_sentences.txt", "w+")
    sampling_sentences = list(node2vec.walks)
    i = 1
    for sentence in sampling_sentences:
        f.write(str(i))
        f.write(":        ")
        i = i + 1
        for word in sentence:
            f.write(word)
            f.write("  ")
        f.write("\n\n")

    f.close()


G = nx.read_multiline_adjlist("convesations.adjlist")


# Part A
"""
     :param G: Input graph
     :param dimensions: Embedding dimensions
     :param walk_length: Number of nodes in each walk
     :param num_walks: Number of walks per node
     :param workers: Number of workers for parallel execution
"""

# Precompute probabilities and generate walks
node2vec = Node2Vec(G, dimensions=64, walk_length=25, num_walks=10, workers=1)  # Use temp_folder for big graphs

# the sampling sentences
make_file_of_sampling_sentences()

# Embed nodes
model = node2vec.fit(window=10, min_count=1, batch_words=4)  # Any keywords acceptable by gensim.Word2Vec can be passed, `diemnsions` and `workers` are automatically passed (from the Node2Vec constructor)

# Look for most similar nodes
for node, enc in model.wv.most_similar('f139aba52f9fa1394b4034a7954b2220'):  # Output node names are always strings
    print(node, enc)

print("vector of f139aba52f9fa1394b4034a7954b2220 is: ")
print(model.wv.get_vector('f139aba52f9fa1394b4034a7954b2220'))
model.wv.save(get_tmpfile("vectors.kv"))

#largest_cc = min(nx.connected_components(G), key=len)
#print(largest_cc)
#print(len(largest_cc))

