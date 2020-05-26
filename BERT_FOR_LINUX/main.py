import networkx as nx
from gensim.models import KeyedVectors
from gensim.test.utils import get_tmpfile
from node2vec import Node2Vec
import bz2
import pickle
import _pickle as cPickle
import clustersBy3DVec
import json2conversation
import Vectors2MatchConversions
import convert_Conversations_2_topic
import sys
sys.path.insert(1, '../Step3')
import Plotter



class Message:
    def __init__(self, author, time, message):
        self.author = author
        self.time = time
        self.message = message
    def __str__(self):
        return "(%s, %s): %s" % (self.author,self.time,self.message)


class Conversation:
    def __init__(self, id, messages):
        self.id = id
        self.messages = messages  # Array of 'Messages' case class
        self.firstAuthor = messages[0].author
        self.secondAuthor = self.getSecondAuthor(self.firstAuthor, messages)

    def __str__(self):
        return "[Conversation] ConversationId: " + self.id + " \n" + "\n".join(
            [str(message) for message in self.messages]) + "\n"

    def getSecondAuthor(self, firstAuthor, messages):
            secondAuthor = self.firstAuthor
            index = 0
            while (secondAuthor == firstAuthor) & (index < len(messages)):
                secondAuthor = messages[index].author
                index = index + 1
            return secondAuthor

    #return list of string (massages) from conversaton
    def getListOfSentences(self):
        result = []
        for message in self.messages:
            if message.message is not None and len(message.message) > 0:#prevent from an empty string to get into the list
                result.append(message.message) # a simple string that represent one sentence
        return result



#the function get name of the json file and return the networkx as appropriate
def load(json_name):
    #making G (networkx)
    if json_name == "pan12-sexual-predator-identification-training-corpus-2012-05-01":
        G = nx.read_multiline_adjlist("adjlists/train_networkxBeforeRemove.adjlist")
    elif json_name == "pan12-sexual-predator-identification-test-corpus-2012-05-17":
        G = nx.read_multiline_adjlist("adjlists/test_networkxBeforeRemove.adjlist")

    return G

#=============================================== embedding functions ================================================#

def embedding(G):
    # Precompute probabilities and generate walks
    node2vec = Node2Vec(G, dimensions=64, walk_length=25, num_walks=10, workers=1)

    # Embed nodes
    model = node2vec.fit(window=10, min_count=1, batch_words=4)

    # Save the model into
    fname = "model.kv"
    path = get_tmpfile(fname)
    model.wv.save(path)

    return model.wv


#========================================initialization of data=========================================#
# Taking G from memory
G = nx.read_multiline_adjlist("./adjlists/train_networkxAfterRemove.adjlist")

# Taking Memory from memory
fname = "model.kv"
path = get_tmpfile(fname)
model = KeyedVectors.load(path, mmap='r')

# the embeding section
# model = embedding(G)

#convert the json file to list of Conversation objects
data = bz2.BZ2File("saved_objects/conversations_train_dataset_after_remove.pbz2", 'rb')  # 40820 conversations
conversations = cPickle.load(data)
print("data conversations amount " + str(len(conversations)))

#=======================================preparing the intut data for bert========================================#
#get centers with name of all
plotter = Plotter.Plotter(G, model)
plotter.SaveAll("/algo_graph")

#get all algorithms dictionary of center by cluster name
(kmeans_centers_by_name,spectral_centers_by_name,connected_center_by_name) = plotter.getAllCentersName()

#make all algorithms dictionary of cluster's nodes by cluster name
clusters = clustersBy3DVec.clustersBy3DVec(kmeans_centers_by_name,spectral_centers_by_name,connected_center_by_name,plotter.all_vectors_after_pca)
print(clusters.makeCombinationsGroups())

# generate set of optional combination. each combination represented by tuple of string
clusters_names = clusters.makeCombinationsGroups()
couple_cluster_names = (list(clusters_names))[0]

## to be delete
for t in clusters_names:
    if len(t) == 2:
        couple_cluster_names = t
        print("find 2 cluster names")
        break

# get list of vectors that matching to the input cluster name
selected_vectors = clusters.getAllVectorsByCombinationClustersName(couple_cluster_names)

print("start process of extracting topic")
# get list of Conversation objects from list of vectors
vectors2Conversations = Vectors2MatchConversions.Vectors2MatchConversions(G, plotter.all_vectors_after_pca, conversations)
selected_conversations = vectors2Conversations.getConversationsFromGroupOfVecs(selected_vectors)

# get list of 5 most similar topics from list of Conversation objects
conversations2Topics = convert_Conversations_2_topic.convert_Conversations_2_topic()
clusters_vector = conversations2Topics.clustersEmbedding(selected_conversations)
topics_list = conversations2Topics.vector2Topic(clusters_vector)
print(topics_list)
print('\007')



