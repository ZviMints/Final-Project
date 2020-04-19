import networkx as nx
import ijson
import matplotlib.pyplot as plt
import pandas as pd



# Zvi Mints and Eilon Tsadok - Windows Version

# Conversation case class
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


def find_second_user(first_user_author, conversation):
    second_user_author = first_user_author
    index = 1
    while (second_user_author  == first_user_author) & (index < len(conversation.messages)):
        second_user = conversation.messages[index].message
        index = index + 1
    return second_user

# Build Graph of conversations
def build_graph(input):
    G = nx.MultiGraph()
    conversations = parse_data_to_case_class(input)
    for conversation in conversations:
            if(conversation.firstAuthor != conversation.secondAuthor):
                G.add_node(conversation.firstAuthor)
                G.add_node(conversation.secondAuthor)
                G.add_edge(conversation.firstAuthor, conversation.secondAuthor)
                print("(%s) --- (%s) Inserted to G" % (conversation.firstAuthor, conversation.secondAuthor))

    print("G with %s totalConnection with %s totalNodes" % (G.number_of_edges(), G.number_of_nodes()))
    return G

def parse_data_to_case_class(input):
    conversations = []
    with open(input["data_path"] + ".json", encoding="utf8") as data:
        print("Successfully opened " + input["data_path"] + ".json...")
        for conversation in ijson.items(data, 'conversations.conversation.item'):
            id = conversation["@id"]
            messages = []
            for message in conversation["message"]:
                messages.append(Message(message["author"], message["time"],message["text"]))
            conversations.append(Conversation(id, messages))
    return conversations


input = {
    "data_path": "C:/Users/EILON/PycharmProjects/data_set/traning/pan12-sexual-predator-identification-training-corpus-2012-05-01/pan12-sexual-predator-identification-training-corpus-2012-05-01",
}

# Building Graph
G = build_graph(input)

# Remove All 2-Connected-Components in G
for component in list(nx.connected_components(G)):
    if len(component) <= 2: # This will actually remove only 2-connected
        for node in component:
            G.remove_node(node)

print("[+] G after remove 2-Connected-Components remains with %s edges and %s nodes" % (G.number_of_edges(), G.number_of_nodes()))
nx.draw(G, node_size = 5)
plt.savefig("conversations.png")
pd.to_pickle(G, "graph_after_remove_2_connected.pkl")
plt.show()

