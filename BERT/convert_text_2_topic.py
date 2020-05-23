import heapq
import pickle
from bert_embedding import BertEmbedding
import numpy as np
import sys

max_val = sys.float_info.max


def load_obj(name):
    with open('saved_objects/' + name + '.pkl', 'rb') as file:
        return pickle.load(file)


def max_top5(top_5_similar):
    max_v, i_max = top_5_similar[0][1], 0
    for counter, couple in enumerate(top_5_similar):
        if couple[1] > max_v:
            max_v = couple[1]
            i_max = counter
    return max_v ,i_max


class convert_text_2_topic:
    def __init__(self):
        self.bert_embedding = BertEmbedding(model='bert_24_1024_16', dataset_name='book_corpus_wiki_en_cased')
        self.vectors_bank_dic = load_obj("Vectors Bank")

    # get conversation (list of sentences) and return bert embedded vector (do not get empty sentence)
    def conversationEmbedding(self, conversation):
        result = self.bert_embedding(conversation)
        sentences_vectors = []
        for sentence in result:  # result = conversation complex vector
            words_vectors = np.array(sentence[1])
            sentence_vector = np.mean(words_vectors,
                                      axis=0)  # one vector for sentence after average on all the words in a sentence
            print(sentence_vector)
            sentences_vectors.append(sentence_vector)

        return np.mean(sentences_vectors, axis=0)


    # get word (string) and return non complex vector
    def wordEmbedding(self, word):
        word = [word.strip()]
        complex_vector = self.bert_embedding(word)
        return np.array(complex_vector[0][1][0])

    #get list of the Conversation object and return bert embedded vector
    def clustersEmbedding(self,cluster):
        conversations_vectors = []
        for conversation in cluster:
            conversations_vectors.append(self.conversationEmbedding(conversation.getListOfSentences()))
        return np.mean(conversations_vectors, axis=0)

    #get an embedded vector and return list of the 5 similar topics
    def vector2Topic(self, vector_result):
        top_5_similar = []
        for i in range(5):
            top_5_similar.append(("name", max_val))
        for name_i, vector_i in self.vectors_bank_dic.items():
            dist = np.linalg.norm(np.array(vector_i) - np.array(vector_result))
            max_v, i_max = max_top5(top_5_similar)
            if max_v > dist:
                top_5_similar[i_max] = (name_i, dist)
        return [name for name in top_5_similar]

