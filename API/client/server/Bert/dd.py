import itertools

a = {}
a["a1"] = [8,9,0]
a["b2"] = [4,5,6]

b = {}
b["k1"] = [8,9,0]
b["r5"] = [4,5,6]
w = [c for c,i in zip(a, range(1))]
w2 = [c for c in b]
mix = []
mix.append([c for c in a])
mix.append([c for c in b])
mmm = w + w2
x = list(itertools.product(*mix))
print(x)
print(tuple(["k1"]))

q = list[tuple([1,2,3]), tuple([2,2,2]), tuple([1,1,1])]
z = list[tuple([1,2]), tuple([2,2]), tuple([1,1])]
q + list[tuple([1,2]), tuple([2,2]), tuple([1,1])]