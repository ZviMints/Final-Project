# Taking G from memory
import math

import networkx
from gensim.models import KeyedVectors
from gensim.test.utils import get_tmpfile

from Step3 import Plotter


def isNodeInside(center,node, R ):
    #find squared distance
    x = math.pow((node[0] - center[0]), 2)
    y = math.pow((node[1] - center[1]), 2)
    z = math.pow((node[2] - center[2]), 2)
    squaredDist = x + y + z  # squared distance between the centre and given point

    return squaredDist < (R ** 2)


def findNodesByCenter(center,R,vectors_3dim):
    nodesAroundCenter = list()
    for node in vectors_3dim:
        if isNodeInside(center,node,R):
            nodesAroundCenter.append(node)
    return nodesAroundCenter

G = networkx.read_multiline_adjlist("./adjlists/graph.adjlist")
# Taking Memory from memory
fname = "model.kv"
path = get_tmpfile(fname)
model = KeyedVectors.load(path, mmap='r')


#get centers with name of all
plotter = Plotter.Plotter(G, model)
(kmeans_centers,spectral_centers,connected_center) = plotter.getAllCentersName()


#making vec 2 id
Vec2Id_dic = {}
for id, vec in zip(G.nodes(),Plotter.BaseGraph.vectors_3dim):
    Vec2Id_dic[vec] = id


