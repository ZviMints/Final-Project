class Vectors2MatchConversions:
    def __init__(self, G, vectors_3dim, conversations):
        self.G = G
        self.vectors_3dim = vectors_3dim
        # making vec 2 id
        self.Vec2Id_dic = {}
        for id, vec in zip(G.nodes(), vectors_3dim):
            self.Vec2Id_dic[tuple(vec)] = id
        self.conversations = conversations

    # return all the Conversation object (list) that match to the input vectors list
    def getConversationsFromGroupOfVecs(self, vecs_list):
        if vecs_list is None:
            return None
        ConversationsByGroupOfVecs = []
        id_set = {self.Vec2Id_dic[tuple(vec)] for vec in vecs_list}  # making set of IDs

        for conversation in self.conversations:
            firstID = conversation.firstAuthor
            secodID = conversation.secondAuthor
            if (firstID in id_set or secodID in id_set):
                ConversationsByGroupOfVecs.append(conversation)
        return ConversationsByGroupOfVecs
