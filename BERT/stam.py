from flask import Flask, session, request
from flask import jsonify
import networkx
from gensim.models import KeyedVectors
from gensim.test.utils import get_tmpfile
from networkx.readwrite import json_graph
import matplotlib.pyplot as plt
from node2vec import Node2Vec
from Step3 import Plotter
import os.path

all_algorithms =["base","kmeans","spectral","connected","kmeans+spectra","kmeans+spectral",
                 "connected+kmeans","kmeans+connected","connected+spectral",
                 "spectral+connected","connected+kmeans+spectral"]
app = Flask(__name__)

# Zvi Mints And Eilon Tsadok
#=============================================== / route ================================================#
@app.route("/")
def index():
    return "Server is UP"

#=============================================== load route ================================================#
@app.route("/load/<string:dataset>", methods=['GET'])
def load(dataset):
    app.logger.info('got ./load request')

    # Making G (networkx)
    if dataset == "pan12-sexual-predator-identification-training-corpus-2012-05-01":
        G = networkx.read_multiline_adjlist("./load/train_networkxBeforeRemove.adjlist")
    elif dataset == "pan12-sexual-predator-identification-test-corpus-2012-05-17":
        G = networkx.read_multiline_adjlist("./load/test_networkxBeforeRemove.adjlist")
    else:
           return jsonify(err="405", msg = "Invalid JSON file name")


    # Generate picture of networkx
    # networkx.draw(G, node_size=1)
    # plt.savefig("./load/results/networkx_before_remove.png")

    # write json formatted data
    app.logger.debug('loaded dataset with %s nodes before remove' % len(G.nodes()))
    before = json_graph.node_link_data(G)  # node-link format to serialize

    # After Remove
    for component in list(networkx.connected_components(G)):
        if len(component) <= 2: # This will actually remove only 2-connected
            for node in component:
                G.remove_node(node)

    # write json formatted data
    app.logger.debug('loaded dataset with %s nodes after remove' % len(G.nodes()))
    after = json_graph.node_link_data(G)  # node-link format to serialize

    # Save after remove graph
    networkx.write_multiline_adjlist(G, "./load/graph.adjlist")

    # Plotting
    networkx.draw(G, node_size=3)
    plt.savefig("./load/networkx_after_remove.png")

    return jsonify(before=before, after=after,before_path="/load/networkx_before_remove.png", after_path="load/networkx_after_remove.png")

#=============================================== embedding route ================================================#
def saveWalks(walks):
    f = open("./embedding/walks.txt", "w+")
    row = 1
    for sentence in walks:
        f.write("row %s:    " % str(row))
        row = row + 1
        for word in sentence:
            f.write(word)
            f.write("  ")
        f.write("\n")
    f.close()

#=============================================== main embedding route ================================================#
@app.route("/embedding", methods=['GET'])
def embedding():
    G = networkx.read_multiline_adjlist("./load/graph.adjlist")

     # Precompute probabilities and generate walks
    node2vec = Node2Vec(G, dimensions=64, walk_length=25, num_walks=10, workers=1)
    saveWalks(list(node2vec.walks))

    # Embed nodes
    model = node2vec.fit(window=10, min_count=1, batch_words=4)

    # Save the model into
    fname = "./embedding/test_embedded_vectors_model.kv"
    path = get_tmpfile(fname)
    model.wv.save(path)

    return jsonify(res = "walks saved successfully", path="/embedding/test_embedded_vectors_model.kv")

#=============================================== pca route ================================================#
@app.route("/pca", methods=['GET'])
def pca():
    skip = True
    for algo in all_algorithms:
        if not os.path.isfile("./pca/" + algo + ".png"):
            skip = False

    if not skip:
        # Taking G from memory
        G = networkx.read_multiline_adjlist("./load/graph.adjlist")

        # Taking Memory from memory
        fname = "./embedding/test_embedded_vectors_model.kv"
        path = get_tmpfile(fname)
        model = KeyedVectors.load(path, mmap='r')

        #PCA from 64D to 3D
        plotter = Plotter.Plotter(G, model)
        all = plotter.getAll()

        for (name, plot) in all:
            plot.savefig("./pca/" + name + ".png")
            app.logger.debug('%s saved in "./pca/" + %s + ".png"' % (name, name))

    return jsonify(res = "pca completed and saved in image", path="/pca/base.png")

#=============================================== result route ================================================#
@app.route("/results/<string:algorithms>", methods=['GET'])

def results(algorithms):
    return jsonify(algorithms=algorithms, path=" /pca/" + algorithms +".png")
