import networkx as nx
from gensim.models import KeyedVectors
from node2vec import Node2Vec
from sklearn import decomposition
from sklearn.preprocessing import StandardScaler
from Community_Detection_With_Algoritms.algorithms import KMeans, BaseGraph, \
    ConnectedComponents, SpectralClustering, Combined
from Community_Detection_With_Algoritms import Plotter
from gensim.test.utils import get_tmpfile
import matplotlib.pyplot as plt

import matplotlib.pyplot

# matplotlib.use('MacOSX')
# Zvi Mints and Eilon Tsadok - Mac Version
#=============================================== load functions ================================================#
#the function get name of the json file and return the networkx as appropriate
def load(json_name):
    #making G (networkx)
    if json_name == "pan12-sexual-predator-identification-training-corpus-2012-05-01":
        G = nx.read_multiline_adjlist("adjlists/train_networkxBeforeRemove.adjlist")
    elif json_name == "pan12-sexual-predator-identification-test-corpus-2012-05-17":
        G = nx.read_multiline_adjlist("adjlists/test_networkxBeforeRemove.adjlist")

    #generate picture of networkx
    nx.draw(G, node_size=5)
    plt.savefig("API_results/load/networkx_before_remove.png")
    # Remove All 2-Connected-Components in G
    for component in list(nx.connected_components(G)):
        if len(component) <= 2: # This will actually remove only 2-connected
            for node in component:
                G.remove_node(node)
    nx.draw(G, node_size=5)
    plt.savefig("API_results/load/networkx_after_remove.png")

    return G

#=============================================== embedding functions ================================================#
def saveWalks(walks):
    f = open("API_results/embedding/walks.txt", "w+")
    row = 1
    for sentence in walks:
        f.write("row %s:    " % str(row))
        row = row + 1
        for word in sentence:
            f.write(word)
            f.write("  ")
        f.write("\n")
    f.close()


def embedding(G):
    # Precompute probabilities and generate walks
    node2vec = Node2Vec(G, dimensions=64, walk_length=25, num_walks=10, workers=1)

    saveWalks(list(node2vec.walks))

    # Embed nodes
    return node2vec.fit(window=10, min_count=1, batch_words=4)


#==========================================  ==========================================#
def main():
    #the load section
    G = load("pan12-sexual-predator-identification-test-corpus-2012-05-17")

    #the embeding section
    model = embedding(G)

    #PCA from 64D to 3D
    plotter = Plotter.Plotter(G, model)
    plt = plotter.BaseGraph.getPlot()
    plt.savefig("API_results/PCA/BaseGraph.png")

    #results
    plt = plotter.kmeans.getPlot()
    plt.savefig("API_results/results/result_cluster.png")

if __name__ == '__main__':
    main()
