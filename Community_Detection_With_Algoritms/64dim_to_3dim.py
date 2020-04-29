import matplotlib as matplotlib
import matplotlib.pyplot as plt
import networkx as nx
import pandas as pd
from gensim.models import KeyedVectors
from gensim.test.utils import get_tmpfile
from sklearn.decomposition import PCA  # From 64dim to 3dim
from sklearn.preprocessing import StandardScaler  # Normalized
from . import Algorithm
matplotlib.use('MacOSX')

# Zvi Mints and Eilon Tsadok - Mac Version

G = nx.read_multiline_adjlist("convesations.adjlist")

fname = "embedded_vectors.kv"
path = get_tmpfile(fname)
model = KeyedVectors.load(path, mmap='r')
vectors_64dim = model.vectors

# Standardizing the features
vectors64_scale = StandardScaler().fit_transform(vectors_64dim)

# PCA Algorithm
pca = PCA(n_components=3)
vectors_3dim = pca.fit_transform(vectors64_scale)


df = pd.DataFrame(vectors_3dim) #  2-dimensional labeled data structure with columns of potentially different types

df['pca-one'] = vectors_3dim[:,0]
df['pca-two'] = vectors_3dim[:,1]
df['pca-three'] = vectors_3dim[:,2]

# Create a scatter plot
figure = plt.figure(dpi= 50, figsize=(160, 100)).gca(projection='3d')
figure.scatter(
    xs=df["pca-one"],
    ys=df["pca-two"],
    zs=df["pca-three"],
    cmap='red'
)


# Plot the Algorithm
Algorithm(vectors_3dim,figure).kmeansPlot()

