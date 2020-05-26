import gzip
import pickle
import Message
import Conversation
import networkx as nx
import ijson
import matplotlib.pyplot as plt
import pandas as pd
import bz2
import pickle
import _pickle as cPickle

# Zvi Mints and Eilon Tsadok - Windows Version


# Build Graph of conversations
def build_graph(input):
    G = nx.MultiGraph()
    conversations = parse_data_to_case_class(input)
    for conversation in conversations:
            if(conversation.firstAuthor != conversation.secondAuthor):
                G.add_node(conversation.firstAuthor)
                G.add_node(conversation.secondAuthor)
                G.add_edge(conversation.firstAuthor, conversation.secondAuthor)
                # print("(%s) --- (%s) Inserted to G" % (conversation.firstAuthor, conversation.secondAuthor))

    print("G with %s totalConnection with %s totalNodes" % (G.number_of_edges(), G.number_of_nodes()))
    return G , conversations

def parse_data_to_case_class(input):
    conversations = []
    with open(input["data_path"] + ".json", encoding="utf8") as data:
        print("Successfully opened " + input["data_path"] + ".json...")
        for conversation in ijson.items(data, 'conversations.conversation.item'):
            id = conversation["@id"]
            messages = []
            for message in conversation["message"]:
                messages.append(Message.Message(message["author"], message["time"], str(message["text"])))
            conversations.append(Conversation.Conversation(id, messages))
    return conversations


input = {
    "data_path": "/mnt/c/Users/EILON/PycharmProjects/data_set/traning"
                 "/pan12-sexual-predator-identification-training-corpus-2012-05-01"
                 "/pan12-sexual-predator-identification-training-corpus-2012-05-01",
}

# Building Graph
G, conversations = build_graph(input)
print("number of conversations before: " + str(len(conversations)))
# with bz2.BZ2File("saved_objects/conversations_train_dataset_before_remove.pbz2", 'w') as f:
#     cPickle.dump(conversations, f)

# Remove All 2-Connected-Components in G
id_to_remove_from_dataset = []
for component in list(nx.connected_components(G)):
    if len(component) <= 2: # This will actually remove only 2-connected
        for node in component:
            G.remove_node(node)
        id_to_remove_from_dataset.append((list(component))[0])
set_id_to_remove = set(id_to_remove_from_dataset)

for index, conv in enumerate(conversations):
    if conv.firstAuthor in set_id_to_remove or conv.secondAuthor in set_id_to_remove:
        del conversations[index]

print("number of conversations after: " + str(len(conversations)))

# with bz2.BZ2File("saved_objects/conversations_train_dataset_after_remove" + ".pbz2", 'w') as f:
#     cPickle.dump(conversations, f)

print("[+] G after remove 2-Connected-Components remains with %s edges and %s nodes" % (G.number_of_edges(), G.number_of_nodes()))