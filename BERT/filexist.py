from bert_serving.client import BertClient

client = BertClient()
vectors = client.encode(["dog"],["cat"],["man"])
print(vectors[1,:])