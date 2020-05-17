class conversations:
    def __init__(self,G,vectors_3dim):
        self.G = G
        self.vectors_3dim = vectors_3dim
        # making vec 2 id
        self.Vec2Id_dic = {}
        for id, vec in zip(G.nodes(), vectors_3dim):
            self.Vec2Id_dic[vec] = id