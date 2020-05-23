from bert_embedding import BertEmbedding
import numpy as np

bert_abstract = """countries world
going to sleep"""

conversation = bert_abstract.split('\n')  # need to create list of sentences
bert_embedding = BertEmbedding(model='bert_24_1024_16', dataset_name='book_corpus_wiki_en_cased')
result = bert_embedding(conversation)

sentences_vectors = []
for sentence in result:  # result = conversation
    words_vectors = np.array(sentence[1])
    sentence_vector = np.mean(words_vectors,
                              axis=0)  # one vector for sentence after average on all the words in a sentence
    sentences_vectors.append(sentence_vector)

conversation_vector = np.mean(sentences_vectors, axis=0)
print(conversation_vector)