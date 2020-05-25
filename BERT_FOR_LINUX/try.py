# # import json2conversation
# # import convert_Conversations_2_topic
# # from bert_embedding import BertEmbedding
# # import numpy as np
# # conversations = json2conversation.json2conversation.parse_data_to_case_class("/mnt/c/Users/EILON/PycharmProjects/data_set/test"
# #                  "/pan12-sexual-predator-identification-test-corpus-2012-05-21"
# #                  "/pan12-sexual-predator-identification-test-corpus-2012-05-17")
# #
# # for conv in conversations:
# #     conversations2Topics = convert_Conversations_2_topic.convert_Conversations_2_topic()
# #     embeded = conversations2Topics.conversationEmbedding(conv)
# #     print(embeded)
# #     break
#
# # conversations2Topics = convert_Conversations_2_topic.convert_Conversations_2_topic()
# # embeded = conversations2Topics.conversationEmbedding(['+arrummzen: you should try soldering it with something', '+ops it is in a laptop?', '+maybe you should try anyway with a screw that has the same dimension like  ----|S|----'])
# # embeded = BertEmbedding(model='bert_24_1024_16', dataset_name='book_corpus_wiki_en_cased')
# # embeded = embeded(["go", "went"])
# #
# #
# # # bert_abstract = """countries world
# # # going to sleep"""
# # from bert_embedding import BertEmbedding
# #
# # bert_abstract = """We introduce a new language representation model called BERT, which stands for Bidirectional Encoder Representations from Transformers.
# #  Unlike recent language representation models, BERT is designed to pre-train deep bidirectional representations by jointly conditioning on both left and right context in all layers.
# #  As a result, the pre-trained BERT representations can be fine-tuned with just one additional output layer to create state-of-the-art models for a wide range of tasks, such as question answering and language inference, without substantial task-specific architecture modifications.
# # BERT is conceptually simple and empirically powerful.
# # It obtains new state-of-the-art results on eleven natural language processing tasks, including pushing the GLUE benchmark to 80.4% (7.6% absolute improvement), MultiNLI accuracy to 86.7 (5.6% absolute improvement) and the SQuAD v1.1 question answering Test F1 to 93.2 (1.5% absolute improvement), outperforming human performance by 2.0%."""
# # sentences = bert_abstract.split('\n')
# # # conversations2Topics = convert_Conversations_2_topic.convert_Conversations_2_topic()
# # # result = conversations2Topics.wordEmbedding("sentences")
# # bert_embedding = BertEmbedding(model='bert_24_1024_16', dataset_name='book_corpus_wiki_en_cased')
# # result = bert_embedding(sentences)
# #
# # print(result)
# import numpy as np
# a = set([tuple([1,2]),tuple([3,4,4]),tuple([2,3,1])])
# b = (np.array(list(a)))
# print(b[0][0])
# # c = b[0]
# # print(c[0])
# # d = tuple([2,3,4])
# # print(d[0])
# # {(1, 2), (3, 4, 4), (2, 3, 1)}
a=[2,3,4,5,6,7,8]
for i,aa in zip(a,range(3)):
    print(i)