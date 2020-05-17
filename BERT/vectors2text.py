class vectors2text:
    def __init__(self,G,vectors_3dim,conversations):
        self.G = G
        self.vectors_3dim = vectors_3dim
        # making vec 2 id
        self.Vec2Id_dic = {}
        for id, vec in zip(G.nodes(), vectors_3dim):
            self.Vec2Id_dic[vec] = id
        self.conversations = conversations

    def getConversationsByGroupOfVecs(self,vecs_list):
        ConversationsByGroupOfVecs = []
        id_set = {self.Vec2Id_dic[vec] for vec in vecs_list}#making set of IDs

        for conversation in self.conversations:
            firstID = conversation.firstAuthor
            secodID = conversation.secondAuthor
            if (firstID in id_set or secodID in id_set):
                ConversationsByGroupOfVecs.append(conversation)
        return ConversationsByGroupOfVecs

