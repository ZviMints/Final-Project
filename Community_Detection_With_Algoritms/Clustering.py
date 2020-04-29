import networkx as nx
from gensim.models import KeyedVectors
from Community_Detection_With_Algoritms import Plotter
from gensim.test.utils import get_tmpfile
from sklearn.decomposition import PCA  # From 64dim to 3dim
from sklearn.preprocessing import StandardScaler  # Normalized
import matplotlib.pyplot

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

# Plot the Algorithm
plt = Plotter.Plotter(vectors_3dim)
# plt.showWithKMeans()
plt.showWithSpectral()

