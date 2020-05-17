

#convert the json file to Conversation object
from BERT.json2conversation import json2conversation

conversations = json2conversation.parse_data_to_case_class("C:/Users/EILON/PycharmProjects/data_set/test"
                 "/pan12-sexual-predator-identification-test-corpus-2012-05-21"
                 "/pan12-sexual-predator-identification-test-corpus-2012-05-17")

convs = set()
convs.add(conversations[1])
convs.add(conversations[1])
convs.add(conversations[2])
convs.add(conversations[3])
print(len(convs))