from grakn.client import GraknClient
import ijson


class conversationWrapper:
    def __init__(self, id, messages):
        self.id = id
        self.messages = messages


def build(input):
    with GraknClient(uri="localhost:48555") as client:
        with client.session(keyspace="conversations_graph") as session:  # graph is the name of the keyspace
            load_data_into_grakn(input, session)


def load_data_into_grakn(input, session):
    print("connected successfully...")
    conversations = parse_data_to_dictionaries(input)  # gets all conversations
    print("got all conversations, starting to process...")
    i = 0
    for conversation in conversations:  # item is now one conversation
        with session.transaction().write() as transaction:
            print("We are looking at conversation number: " + i )
            i = i + 1
            (firstQuery, first_user_id) = insertFirstUser(conversation)
            (secondQuery, second_user_id) = insertSecondUser(conversation)
            (thirdQuery) = createConnectedRelation(conversation, first_user_id, second_user_id)

            print("Executing Graql Query: " + firstQuery)
            transaction.query(firstQuery)

            print("Executing Graql Query: " + secondQuery)
            transaction.query(secondQuery)

            print("Executing Graql Query: " + thirdQuery)
            transaction.query(thirdQuery)

            transaction.commit()

    print("\nInserted " + str(len(conversations)) + " items from [ " + input["data_path"] + "] into Grakn.\n")


# Insert first Author at conversation
def insertFirstUser(conversation):
    first_user_id = conversation.messages[0]["author"]
    return ('insert $user isa user, has user_id "' + first_user_id + '";', first_user_id)


# Insert second Author at conversation
def insertSecondUser(conversation):
    # loop to find the second user
    first_user_id = conversation.messages[0]["author"]
    second_user_id = first_user_id
    index = 0
    while second_user_id == first_user_id:
        second_user_id = conversation.messages[index]["author"]
        index = index + 1

        return ('insert $user isa user, has user_id "' + second_user_id + '";', second_user_id)


# Create connection between first author and second author
def createConnectedRelation(conversation, first_user_id, second_user_id):
    # Match first user
    graql_insert_query = 'match $user1 isa user, has user_id "' + first_user_id + '";'
    # Match  second user
    graql_insert_query += '$user2 isa user, has user_id "' + second_user_id + '";'
    # insert connected relation
    graql_insert_query += 'insert $new-connection(talk: $user1, talk: $user2) isa connected; $new-connection has conversation_id "' + conversation.id + '"; '  # [V]
    return graql_insert_query


def parse_data_to_dictionaries(input):
    conversations = []
    with open(input["data_path"] + ".json") as data:
        print("successfully opened " + input["data_path"] + ".json")
        for root in ijson.items(data, 'conversations.conversation'):  #
            for conversation in root:
                id = conversation["@id"]
                messages = []
                for msg in conversation["message"]:
                    messages.append(msg)
                conversations.append(conversationWrapper(id, messages))
                print("added conversation number: " + id)
    return conversations


input = {
    "data_path": "/Users/Zvi/Desktop/FinalProject/Dataset/pan12-sexual-predator-identification-training-corpus-2012-05-01/small_train",
}

# build_conversations_graph(input)
build(input)

