import networkx as nx
import ijson
import matplotlib.pyplot as plt



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
    conversations = parse_data_to_case_class(input) # Parse to case class
    totalConnection = 0
    totalNodes = 0
    for conversation in conversations:
            if(conversation.firstAuthor != conversation.secondAuthor):
                G.add_node(conversation.firstAuthor)
                G.add_node(conversation.secondAuthor)
                G.add_edge(conversation.firstAuthor, conversation.secondAuthor)
                print("(%s) --- (%s) Inserted to G" % (conversation.firstAuthor, conversation.secondAuthor))
                totalConnection = totalConnection + 1
                totalNodes = totalNodes + 2
            else:
                totalNodes  = totalNodes + 1
    print("G with %s totalConnection with %s totalNodes" % (totalConnection, totalNodes))
    return G

def parse_data_to_case_class(input):
    conversations = []
    with open(input["data_path"] + ".json", encoding="utf8") as data:
        print("Successfully opened " + input["data_path"] + ".json...")
        i=0
        for conversation in ijson.items(data, 'conversations.conversation.item'):
            i = i +1
            if i ==10000:
                break
            id = conversation["@id"]
            messages = []
            for message in conversation["message"]:
                messages.append(Message(message["author"], message["time"],message["text"]))
            conversations.append(Conversation(id, messages))
    return conversations


input = {
    "data_path": "C:/Users/EILON/PycharmProjects/data_set/test/pan12-sexual-predator-identification-test-corpus-2012-05-21/pan12-sexual-predator-identification-test-corpus-2012-05-17",
}

# Building Graph
G = build_graph(input)

# Plot
nx.draw(G , node_size = 0.5)

# Show Graph
plt.show()