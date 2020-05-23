import networkx
from gensim.models import KeyedVectors
from gensim.test.utils import get_tmpfile

from BERT.clustersBy3DVec import clustersBy3DVec
from BERT.json2conversation import json2conversation
from BERT.vectors2text import Vectors2MatchConversions
from Step3 import Plotter


#========================================initialization of data=========================================#
# Taking G from memory
G = networkx.read_multiline_adjlist("./adjlists/graphU.adjlist")
# Taking Memory from memory
fname = "model.kv"
path = get_tmpfile(fname)
model = KeyedVectors.load(path, mmap='r')

#convert the json file to list of Conversation objects
conversations = json2conversation.parse_data_to_case_class("C:/Users/EILON/PycharmProjects/data_set/test"
                 "/pan12-sexual-predator-identification-test-corpus-2012-05-21"
                 "/pan12-sexual-predator-identification-test-corpus-2012-05-17")


#=======================================preparing the intut data for bert========================================#
#get centers with name of all
plotter = Plotter.Plotter(G, model)

#get all algorithms dictionary of center by cluster name
(kmeans_centers_by_name,spectral_centers_by_name,connected_center_by_name) = plotter.getAllCentersName()

#make all algorithms dictionary of cluster's nodes by cluster name
clusters = clustersBy3DVec(kmeans_centers_by_name,spectral_centers_by_name,connected_center_by_name,plotter.all_vectors_after_pca)

#get list of vectors that matching to the input cluster name
selected_vectors = clusters.getAllVectorsByCombinationClustersName(["K2"])

#get list of Conversation objects from list of vectors
vectors2text = Vectors2MatchConversions(G, plotter.all_vectors_after_pca, conversations)
selected_conversations = vectors2text.getConversationsByGroupOfVecs(selected_vectors)

# #get list of 5 most similar topics from list of Conversation objects
# conversations2Topics = convert_text_2_topic()
# clusters_vector = conversations2Topics.clustersEmbedding(selected_conversations)
# topics_list = conversations2Topics.vector2Topic(clusters_vector)

print(len(selected_conversations))
for conv in selected_conversations:
    for massage_obj in conv.messages:
        print(massage_obj.message)

