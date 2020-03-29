from grakn.client import GraknClient
import ijson

def build_phone_call_graph(input): # Step 2
    with GraknClient(uri="localhost:48555") as client:
        with client.session(keyspace = "graph") as session: # graph is the name of the keyspace
                load_data_into_grakn(input, session)

def load_data_into_grakn(input, session): # Step 3
    conversations = parse_data_to_dictionaries(input) # gets all conversations

    for conversation in conversations: # item is now one conversation
        with session.transaction().write() as transaction:
            graql_insert_query = input["template"](conversation)
            print("Executing Graql Query: " + graql_insert_query)
            transaction.query(graql_insert_query)
            transaction.commit()

    print("\nInserted " + str(len(conversations)) + " items from [ " + input["data_path"] + "] into Grakn.\n")

def conversation_template(conversation):
    # insert conversation

    # Safety check if message list is empty then return
    first_user_id = "" # First author
    graql_insert_query = 'insert $user isa person, has user_id "' + first_user_id

    # loop to find the second user
    second_user_id = "" # Second author
    graql_insert_query = 'insert $user isa person, has user_id "' + second_user_id


    # Need to initialize relation between the two users with "play talk"

    # Need to initialize connected relation with "@id"

    # Match company | first user
    graql_insert_query = 'match #user isa company, has user_id "' + first_user_id + ';'
    # Match person | second user
    graql_insert_query += 'match #user isa company, has user_id "' + second_user_id + ';'
    # insert contract | connected relation
    graql_insert_query += " insert (talk: $user, talk: $user) isa connected, has conversation_id " + conversation["@id"] + ';'



    # ------------------------- Correct
    graql_insert_query = 'insert $person isa person, has phone-number "' + person["phone_number"] + '"'
    if "first_name" in person:
        # person is a customer
        graql_insert_query += ", has is-customer true"
        graql_insert_query += ', has first-name "' + person["first_name"] + '"'
        graql_insert_query += ', has last-name "' + person["last_name"] + '"'
        graql_insert_query += ', has city "' + person["city"] + '"'
        graql_insert_query += ", has age " + str(person["age"])
    else:
        # person is not a customer
        graql_insert_query += ", has is-customer false"
    graql_insert_query += ";"
    return graql_insert_query

def parse_data_to_dictionaries(input): # Step 4
    items = []
    with open(input["data_path"] + ".json") as data:
        for item in ijson.items(data, "item"):
            items.append(item)
    return items

input = {
        "data_path": "files/phone-calls/data/people",
        "template": conversation_template
}

build_phone_call_graph(input) # Step 1