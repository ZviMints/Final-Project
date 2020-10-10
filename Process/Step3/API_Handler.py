import networkx
import networkx as nx
from gensim.models import KeyedVectors
from gensim.test.utils import get_tmpfile
from node2vec import Node2Vec
from Step3 import Plotter
# import Plotter
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
    # nx.draw(G, node_size=1)
    # plt.savefig("../API/client/public/models/load/networkx_before_remove.png")
    # Remove All 2-Connected-Components in G
    for component in list(nx.connected_components(G)):
        if len(component) <= 2:# This will actually remove only 2-connected
            for node in component:
                G.remove_node(node)
    networkx.write_multiline_adjlist(G, "./adjlists/graphU.adjlist")
    # nx.draw(G, node_size=3)
    # plt.savefig("../API/client/public/models/load/networkx_after_remove.png")
    return G

#=============================================== embedding functions ================================================#
def saveWalks(walks):
    f = open("../API/client/public/models/embedding/walks.txt", "w+")
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

    # saveWalks(list(node2vec.walks))

    # Embed nodes
    model = node2vec.fit(window=10, min_count=1, batch_words=4)

    # Save the model into
    fname = "model.kv"
    path = get_tmpfile(fname)
    model.wv.save(path)

    return model.wv

#==========================================  ==========================================#
def main():
    # #the load section
    # G = load("pan12-sexual-predator-identification-test-corpus-2012-05-17")
    #
    # #the embeding section
    # model = embedding(G)

    # Taking G from memory
    G = networkx.read_multiline_adjlist("./adjlists/graphU.adjlist")
    # Taking Memory from memory
    fname = "model.kv"
    path = get_tmpfile(fname)
    model = KeyedVectors.load(path, mmap='r')

    #PCA from 64D to 3D
    plotter = Plotter.Plotter(G, model)
    plot = plotter.BaseGraph.getPlot()
    # plot.savefig("API_handler_results/BaseGraph.png")

    #results
    plotter.spectral.getPlot().show()
    plotter.kmeans.getPlot().show()
    plotter.Combined.getPlot("kmeans+spectral+connected").show()
    plot = plotter.Combined.getPlot("kmeans+connected")
    plot.savefig("API_handler_results/result_cluster.png")


if __name__ == '__main__':
    main()
