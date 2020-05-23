import pickle
import convert_text_2_topic


def save_obj(obj, name):
    with open('saved_objects/' + name + '.pkl', 'wb') as file:
        pickle.dump(obj, file, pickle.HIGHEST_PROTOCOL)


text2Topic = convert_text_2_topic.convert_text_2_topic()
vectors_bank = {}
in_file = open("vocab.txt")
for line in in_file.readlines():
    word_vector = text2Topic.wordEmbedding(line)
    vectors_bank[line.strip()] = word_vector

save_obj(vectors_bank, "Vectors Bank")

