import convert_Conversations_2_topic
import bz2
import _pickle as cPickle


# def save_obj(obj, name):
#     with open('saved_objects/' + name + '.pkl', 'wb') as file:
#         pickle.dump(obj, file, pickle.HIGHEST_PROTOCOL)


text2Topic = convert_Conversations_2_topic.convert_Conversations_2_topic()
vectors_bank = {}
in_file = open("../data/bert/vocab_update.txt")
for line in in_file.readlines():
    word_vector = text2Topic.wordEmbedding(line)
    vectors_bank[line.strip()] = word_vector

# save_obj(vectors_bank, "word2vec")

# saving a compress pickle file
with bz2.BZ2File("word2vectorUpdate.pbz2", 'w') as f:
    cPickle.dump(vectors_bank, f)
