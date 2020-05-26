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
import os
import bz2
from Bert import clustersBy3DVec
import _pickle as cPickle
# =============================================== models ================================================ #
class Message:
    def _init_(self, author, time, message):
        self.author = author
        self.time = time
        self.message = message
    def _str_(self):
        return "(%s, %s): %s" % (self.author,self.time,self.message)

class Conversation:
    def _init_(self, id, messages):
        self.id = id
        self.messages = messages  # Array of 'Messages' case class
        self.firstAuthor = messages[0].author
        self.secondAuthor = self.getSecondAuthor(self.firstAuthor, messages)

    def _str_(self):
        return "[Conversation] ConversationId: " + self.id + " \n" + "\n".join(
            [str(message) for message in self.messages]) + "\n"

    def getSecondAuthor(self, firstAuthor, messages):
            secondAuthor = self.firstAuthor
            index = 0
            while (secondAuthor == firstAuthor) & (index < len(messages)):
                secondAuthor = messages[index].author
                index = index + 1
            return secondAuthor

#=============================================== main app ================================================#
# Configurations
all_algorithms =["base","kmeans","spectral","connected","kmeans+spectral","connected+kmeans","connected+spectral","connected+kmeans+spectral"]

app = Flask(__name__, static_url_path = "/data", static_folder = "data")

# Zvi Mints And Eilon Tsadok
#=============================================== load route ================================================#
@app.route("/load", methods=['POST'])
def load():
    # Getting datset from request
    dataset = request.get_json()["dataset"]
    # If use server data or do all process
    useServerData = request.get_json()["useServerData"]
    # Prefix for saving information
    prefix = "/data" + "/load/" + dataset

    skip = True
    if not os.path.isfile("." + prefix + "/networkx_after_remove.png"):  # and os.path.isfile("." + prefix + dataset + "/networkx_before_remove.png"):
        skip = False

    if not useServerData:
        skip = False

    app.logger.info('got /load request with skip = %s and dataset = %s' % (skip,dataset))

    # Making G (networkx)
    if dataset == "pan12-sexual-predator-identification-training-corpus-2012-05-01":
        G = networkx.read_multiline_adjlist("./data/start/train_networkxBeforeRemove.adjlist")

    elif dataset == "pan12-sexual-predator-identification-test-corpus-2012-05-17":
        G = networkx.read_multiline_adjlist("./data/start/test_networkxBeforeRemove.adjlist")
    else:
           return jsonify(err="405", msg = "Invalid JSON file name")

    # if not skip:
    #    # Plotting
    #    networkx.draw(G, node_size=1)
    #    plt.savefig("." + prefix + "/networkx_before_remove.png")

    # write json formatted data
    app.logger.debug('loaded dataset with %s nodes before remove' % len(G.nodes()))
    before = json_graph.node_link_data(G)["links"]  # node-link format to serialize
    graphData = []
    graphData.append("%s Nodes, %s links" % (len(G.nodes()),len(G.edges())))

    # After Remove
    for component in list(networkx.connected_components(G)):
        if len(component) <= 2: # This will actually remove only 2-connected
            for node in component:
                G.remove_node(node)

    # write json formatted data
    app.logger.debug('loaded dataset with %s nodes after remove' % len(G.nodes()))
    after = json_graph.node_link_data(G)["links"]  # node-link format to serialize
    graphData.append("%s Nodes, %s links" % (len(G.nodes()),len(G.edges())))

    # Save after remove graph
    if not os.path.exists("." + prefix):
        os.makedirs("." + prefix)
    networkx.write_multiline_adjlist(G, "." + prefix + "/graph.adjlist")
    if not skip:
        # Plotting
        networkx.draw(G, node_size=3)
        plt.savefig("." + prefix + "/networkx_after_remove.png")

    return jsonify(before_path= prefix + "/networkx_before_remove.png", after_path = prefix + "/networkx_after_remove.png", before = before, after = after, graphData = graphData)

#=============================================== embedding route ================================================#
def saveWalks(walks,prefix):
    if not os.path.exists("." + prefix):
        os.makedirs("." + prefix)
    f = open("." + prefix +"/walks.txt", "w+")
    row = 1
    for sentence in walks:
        f.write("row %s:" % str(row))
        row = row + 1
        for word in sentence:
            f.write(word)
            f.write(" ")
        f.write("\n")
    f.close()

@app.route("/embedding", methods=['POST'])
def embedding():
    # Getting datset from request
    dataset = request.get_json()["dataset"]
    # If use server data or do all process
    useServerData = request.get_json()["useServerData"]
    # Prefix for saving information
    prefix = "/data" + "/embedding/" + dataset

    skip = True
    print("." + prefix  + "/walks.txt")
    if not os.path.isfile("." + prefix  + "/walks.txt"):
        skip = False

    if not useServerData:
        skip = False

    app.logger.info('got /embedding request with skip = %s and dataset = %s' % (skip,dataset))

    if not skip:
        G = networkx.read_multiline_adjlist("." + "/data" + "/load/" + dataset + "/graph.adjlist")

         # Precompute probabilities and generate walks
        node2vec = Node2Vec(G, dimensions=64, walk_length=25, num_walks=10, workers=1)
        saveWalks(list(node2vec.walks),prefix)

        # Embed nodes
        model = node2vec.fit(window=10, min_count=1, batch_words=4)

        # Save the model into
        fname = "model.kv"
        path = get_tmpfile(fname)
        model.wv.save(path)

    return jsonify(res = "walks saved successfully", walk_length = 25, num_walks = 10, walks = open("." + prefix + "/walks.txt", "r").read())

#=============================================== pca route ================================================#
@app.route("/pca", methods=['POST'])
def pca():
    # Getting datset from request
    dataset = request.get_json()["dataset"]
    # If use server data or do all process
    useServerData = request.get_json()["useServerData"]
    # Prefix for saving information
    prefix = "/data" + "/pca/" + dataset

    if not os.path.exists("." + prefix):
        os.makedirs("." + prefix)

    skip = True
    for algo in all_algorithms:
        if not os.path.isfile("." + prefix + "/" + algo + ".png"):
            skip = False

    if not useServerData:
        skip = False

    app.logger.info('got /pca request with skip = %s and dataset = %s' % (skip,dataset))

    if not skip:
        # Taking G from memory
        G = networkx.read_multiline_adjlist("." + "/data" + "/load/" + dataset + "/graph.adjlist")

        # Taking Memory from memory
        fname = "model.kv"
        path = get_tmpfile(fname)
        model = KeyedVectors.load(path, mmap='r')

        # PCA from 64D to 3D
        plotter = Plotter.Plotter(G, model)
        plotter.SaveAll(prefix)

    return jsonify(res = "pca completed and saved in image", path = prefix + "/base.png")

#=============================================== result route ================================================#
@app.route("/results", methods=['POST'])
def results():
    # Getting datset from request
    dataset = request.get_json()["dataset"]
    # Getting algorithms from request
    algorithms = request.get_json()["algorithms"]

    app.logger.info('got /results request with dataset = %s and algorithms = %s' % (dataset,algorithms))

    return jsonify(path=  "/data/pca/" + dataset + "/" + algorithms + ".png")

#=============================================== bert route ================================================#
@app.route("/getLabels", methods=['POST'])
def getLabels():
        # Getting datset from request
        dataset = request.get_json()["dataset"]
        # If use server data or do all process
        useServerData = request.get_json()["useServerData"]
        # Prefix for saving information
        prefix = "/data" + "/bert/" + dataset

        skip = True
        if not os.path.isfile("todo"):
            skip = False

        if not useServerData:
            skip = False

        app.logger.info('got /getLabels request with skip = %s and dataset = %s' % (skip,dataset))
        if not skip:
            # Taking G from memory
            G = networkx.read_multiline_adjlist("." + "/data" + "/load/" + dataset + "/graph.adjlist")

            # Taking Memory from memory
            fname = "model.kv"
            path = get_tmpfile(fname)
            model = KeyedVectors.load(path, mmap='r')

            #convert the json file to list of Conversation objects
            if dataset == "pan12-sexual-predator-identification-training-corpus-2012-05-01":
                data = bz2.BZ2File("./data/start/" + "conversations_train_dataset_after_remove.pbz2", 'rb')  # 40820 conversations
            elif dataset == "pan12-sexual-predator-identification-test-corpus-2012-05-17":
                data = bz2.BZ2File("./data/start/" + "conversations_test_dataset_after_remove.pbz2", 'rb')  # 40820 conversations

            conversations = cPickle.load(data) # List of conversations object
            # plotter = Plotter.Plotter(G, model)
            #
            # # Bert Starting Here
            #
            # # Get all algorithms dictionary of center by cluster name
            # (kmeans_centers_by_name,spectral_centers_by_name,connected_center_by_name) = plotter.getAllCentersName()
            #
            # # Make all algorithms dictionary of cluster's nodes by cluster name
            # clusters = clustersBy3DVec.clustersBy3DVec(kmeans_centers_by_name,spectral_centers_by_name,connected_center_by_name,plotter.all_vectors_after_pca)
            #
            # # Generate set of all possible combination. each combination represented by immutable list of string
            # clusters_names = clusters.makeCombinationsGroups()
            # return clusters_names
            return "working"



@app.route("/bert", methods=['POST'])
def bert():
    dataset = request.get_json()["dataset"]
    cluster = request.get_json()["cluster"] # K6
    information = "cool cluster"
    return jsonify(information = information)
