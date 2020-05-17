import math
import numpy as np

R = 3

def isNodeInside(center, node):
    # find squared distance
    x = math.pow((node[0] - center[0]), 2)
    y = math.pow((node[1] - center[1]), 2)
    z = math.pow((node[2] - center[2]), 2)
    squaredDist = x + y + z  # squared distance between the centre and given point

    return squaredDist < (R ** 2)



class clustersBy3DVec:
    def __init__(self,kmeans_centers,spectral_centers,connected_center,vectors_3dim):
        self.vectors_3dim = vectors_3dim
        self.kmeans_clusters = self.convertCenters2ClustersOfVecs(kmeans_centers)
        self.spectral_clusters = self.convertCenters2ClustersOfVecs(spectral_centers)
        self.connected_clusters = self.convertCenters2ClustersOfVecs(connected_center)


    def findNodesByCenter(self,center):
        nodesAroundCenter = []
        for node in self.vectors_3dim:
            if isNodeInside(center, node):
                nodesAroundCenter.append(node)
        return np.array(nodesAroundCenter)

    # return list of centers with their names and return dictionary of center's name and all the vecs(nodes) inside
    def convertCenters2ClustersOfVecs(self,centers):
        clustersOfVecsByCentersName = {}
        for name, center in centers.items():
            clustersOfVecsByCentersName[name] = self.findNodesByCenter(center)
        return clustersOfVecsByCentersName

    #return list of vectors that matching to the input cluster name
    def getAllVectorsByClusterName(self,name):
        if len(name) > 1:
            if name[0] == "K" and name[1:].isdigit() and int(name[1:]) < len(self.kmeans_clusters):
                return self.kmeans_clusters[name]
            elif name[0] == "S" and name[1:].isdigit() and int(name[1:]) < len(self.spectral_clusters):
                return self.spectral_clusters[name]
            elif name[0] == "C" and name[1:].isdigit() and int(name[1:]) < len(self.connected_clusters):
                return self.connected_clusters[name]
        return None

    # get list of vectors that matching to the combination of the input clusters name
    def getAllVectorsByCombinationClustersName(self,name):
        return None#need to finish


