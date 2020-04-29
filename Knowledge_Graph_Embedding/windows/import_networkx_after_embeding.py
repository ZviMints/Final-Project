import networkx as nx
import matplotlib as matplotlib
from node2vec import Node2Vec
from gensim.test.utils import get_tmpfile
from gensim.models import KeyedVectors

# Zvi Mints and Eilon Tsadok - Mac Version


word_vectors = KeyedVectors.load(get_tmpfile("vectors.kv"), mmap='r')
# Look for most similar nodes
for node, enc in word_vectors.most_similar('e5cf84ed9ede55d365d58a0ca651edd3'):  # Output node names are always strings
    print(node, enc)

print("vector of f139aba52f9fa1394b4034a7954b2220 is: ", word_vectors.get_vector('f139aba52f9fa1394b4034a7954b2220'))

