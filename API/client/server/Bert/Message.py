
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
