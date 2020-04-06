import networkx as nx
import ijson
import matplotlib.pyplot as plt

class conversationWrapper:
    def __init__(self, id, messages):
        self.id = id
        self.messages = messages


def build_graph():
    G = nx.Graph()
    conversations = parse_data_to_dictionaries(input)
    i = 0
    for conversation in conversations:
        first_user = conversation.messages[0]["author"]
        second_user = find_second_user(conversation)
        if first_user!= second_user:
            G.add_node(first_user)
            G.add_node(second_user)
            G.add_edge(first_user, second_user)
            i = i+1
            print(i)
    return G

def parse_data_to_dictionaries(input):
    conversationsWrapper = []
    with open(input["data_path"] + ".json", encoding="utf8") as data:
        print("successfully opened " + input["data_path"] + ".json")
        for conversation in ijson.items(data, 'conversations.conversation.item'):
            id = conversation["@id"]
            messages = []
            for msg in conversation["message"]:
                messages.append(msg)
            conversationsWrapper.append(conversationWrapper(id, messages))
            print("added conversation number: " + id)
    return conversationsWrapper


def find_second_user(conversation):
    first_user_id = conversation.messages[0]["author"]
    second_user_id = first_user_id
    index = 1
    while (second_user_id == first_user_id) & (index < len(conversation.messages)):
        second_user_id = conversation.messages[index]["author"]
        index = index + 1
    return second_user_id

input = {
    "data_path": "C:/Users/EILON/PycharmProjects/data_set/traning/pan12-sexual-predator-identification-training-corpus-2012-05-01/pan12-sexual-predator-identification-training-corpus-2012-05-01",
}

G = build_graph()
nx.draw(G)
plt.show()