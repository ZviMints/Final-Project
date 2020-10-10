# Conversation case class
import ijson
import Message
import Conversation


def parse_data_to_case_class(input):
    conversations = []
    with open(input + ".json", encoding="utf8") as data:
        print("Successfully opened " + input + ".json...")
        for conversation in ijson.items(data, 'conversations.conversation.item'):
            id = conversation["@id"]
            messages = []
            for message in conversation["message"]:
                messages.append(Message.Message(message["author"], message["time"], str(message["text"])))
            conversations.append(Conversation.Conversation(id, messages))
    return conversations
