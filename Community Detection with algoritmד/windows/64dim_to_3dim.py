import networkx as nx
import matplotlib as matplotlib
import matplotlib.pyplot as plt
from node2vec import Node2Vec
from gensim.test.utils import get_tmpfile
from gensim.models import KeyedVectors
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
import pandas as pd
import numpy as np

# Zvi Mints and Eilon Tsadok - Mac Version

G = nx.read_multiline_adjlist("convesations.adjlist")
word_vectors = KeyedVectors.load(get_tmpfile("vectors.kv"), mmap='r')
vectors64 = word_vectors.vectors


# Standardizing the features
vectors64_scale = StandardScaler().fit_transform(vectors64)

pca = PCA(n_components=3)

pca_result = pca.fit_transform(vectors64_scale)
#principalDf = pd.DataFrame(data = principalComponents
 #            , columns = ['principal component 1', 'principal component 2', 'principal component 3'])


df = pd.DataFrame(pca_result)

df['pca-one'] = pca_result[:, 0]
df['pca-two'] = pca_result[:, 1]
df['pca-three'] = pca_result[:, 2]

# For reproducability of the results
# np.random.seed(42)
# rndperm = np.random.permutation(df.shape[0])

ax = plt.figure(dpi= 50, figsize=(160,100)).gca(projection='3d')
ax.scatter(
    xs=df["pca-one"],
    ys=df["pca-two"],
    zs=df["pca-three"],
    cmap='red'
)
km = KMeans(n_clusters=4, init='k-means++', max_iter=300, n_init=10, random_state=0)
km.fit_predict(pca_result)
ax.scatter(km.cluster_centers_[:, 0], km.cluster_centers_[:, 1], km.cluster_centers_[:, 2], s=10000, c='red')
ax.set_xlabel('pca-one')
ax.set_ylabel('pca-two')
ax.set_zlabel('pca-three')
plt.show()

