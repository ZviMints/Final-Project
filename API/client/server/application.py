
import logging
from flask import Flask, render_template
from flask import jsonify

import networkx as nx
from node2vec import Node2Vec
import matplotlib.pyplot as plt

app = Flask(__name__)

# Zvi Mints And Eilon Tsadok

@app.route("/graph")
def graph():
    return jsonify("this is text that i get from backend via Flask framework (here will be the graph)")

#=============================================== load route ================================================#
@app.route("/load/<string:dataset>", methods=['GET'])
def load(dataset):
    app.logger.info('got ./load request')

    #making G (networkx)
    if dataset == "pan12-sexual-predator-identification-training-corpus-2012-05-01":
        G = nx.read_multiline_adjlist("./load/train_networkxBeforeRemove.adjlist")
    elif dataset == "pan12-sexual-predator-identification-test-corpus-2012-05-17":
        G = nx.read_multiline_adjlist("./load/test_networkxBeforeRemove.adjlist")
    else:
           return jsonify(err="405 Method Not Allowed")

    # Generate picture of networkx
#    nx.draw(G, node_size=1)
#    matplotlib.pyplot.savefig("../public/models/load/models/load/networkx_before_remove.png")
    app.logger.debug('loaded dataset with %s nodes before remove' % len(G.nodes()))

    # After Remove
    for component in list(nx.connected_components(G)):
        if len(component) <= 2: # This will actually remove only 2-connected
            for node in component:
                G.remove_node(node)

    app.logger.debug('loaded dataset with %s nodes after remove' % len(G.nodes()))

    nx.draw(G, node_size=3)
    plt.savefig("../API/client/public/models/load/networkx_after_remove.png")

    return jsonify(before="networkx_before_remove.png", after="networkx_after_remove.png")
