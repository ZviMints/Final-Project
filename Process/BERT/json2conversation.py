# Conversation case class
import ijson


class Message:
    def __init__(self, author, time, message):
        self.author = author
        self.time = time
        self.message = message
    def __str__(self):
        return "(%s, %s): %s" % (self.author,self.time,self.message)

def find_second_user(first_user_author, conversation):
    second_user_author = first_user_author
    index = 1
    while (second_user_author  == first_user_author) & (index < len(conversation.messages)):
        second_user = conversation.messages[index].message
        index = index + 1
    return second_user

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

    def getListOfSentences(self):
        result = []
        for massage in self.messages:
            if len(massage.message) > 0:#prevent from an empty string to get into the list
                result.append(massage.message) # a simple string that represent one sentence
        return result

class json2conversation:
    def parse_data_to_case_class(input):
        conversations = []
        with open(input + ".json", encoding="utf8") as data:
            print("Successfully opened " + input + ".json...")
            for conversation in ijson.items(data, 'conversations.conversation.item'):
                id = conversation["@id"]
                messages = []
                for message in conversation["message"]:
                    messages.append(Message(message["author"], message["time"],message["text"]))
                conversations.append(Conversation(id, messages))
        return conversations
