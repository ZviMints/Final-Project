import math
import numpy as np
import itertools

R = 2.4
MIN_NODES_FOR_MATCH = 1


def isNodeInside(center, node):
    # find squared distance
    x = math.pow((node[0] - center[0]), 2)
    y = math.pow((node[1] - center[1]), 2)
    z = math.pow((node[2] - center[2]), 2)
    squaredDist = x + y + z  # squared distance between the centre and given point

    return squaredDist < (R ** 2)


def findMatchVectors(first_cluster_vectors, second_cluster_vectors):
    if first_cluster_vectors is None or second_cluster_vectors is None:
        return None
    matchVectors = []
    for vector in first_cluster_vectors:
        if vector in second_cluster_vectors:
            matchVectors.append(vector)
    if len(matchVectors) < MIN_NODES_FOR_MATCH:
        print("you insert illegal combination")
        return None
    return np.array(list(matchVectors))


class clustersBy3DVec:
    def __init__(self, kmeans_centers, spectral_centers, connected_center, vectors_3dim):
        self.vectors_3dim = vectors_3dim
        self.kmeans_clusters = self.convertCenters2ClustersOfVecs(kmeans_centers)
        self.spectral_clusters = self.convertCenters2ClustersOfVecs(spectral_centers)
        self.connected_clusters = self.convertCenters2ClustersOfVecs(connected_center)

    def findNodesByCenter(self, center):
        nodesAroundCenter = []
        for node in self.vectors_3dim:
            if isNodeInside(center, node):
                nodesAroundCenter.append(node)
        return np.array(nodesAroundCenter)

    # the input is list of centers with their names and return dictionary of center's name and all the vecs(nodes) inside
    def convertCenters2ClustersOfVecs(self, centers):
        clustersOfVecsByCentersName = {}
        for name, center in centers.items():
            clustersOfVecsByCentersName[name] = self.findNodesByCenter(center)
        return clustersOfVecsByCentersName

    # return list of vectors that matching to the input cluster name
    def getAllVectorsBySingleClusterName(self, name):
        if len(name) > 1:
            if name[0] == "K" and name[1:].isdigit() and int(name[1:]) < len(self.kmeans_clusters):
                return self.kmeans_clusters[name]
            elif name[0] == "S" and name[1:].isdigit() and int(name[1:]) < len(self.spectral_clusters):
                return self.spectral_clusters[name]
            elif name[0] == "C" and name[1:].isdigit() and int(name[1:]) < len(self.connected_clusters):
                return self.connected_clusters[name]
        print("you insert illegal name")
        return None

    # get list of vectors that matching to the combination of the input clusters name
    def getAllVectorsByCoupleClustersName(self, name1, name2):
        first_cluster_vectors = self.getAllVectorsBySingleClusterName(name1)
        second_cluster_vectors = self.getAllVectorsBySingleClusterName(name2)
        if (first_cluster_vectors is not None and second_cluster_vectors is not None):
            return findMatchVectors(first_cluster_vectors, second_cluster_vectors)
        return None

    # can handle any kind of clusters names combination(a combination represented by list of string),
    # return a matching list of vectors
    def getAllVectorsByCombinationClustersName(self, cluster_names_tuple):
        combination_size = len(cluster_names_tuple)
        if combination_size == 1:
            return self.getAllVectorsBySingleClusterName(cluster_names_tuple[0])
        if combination_size == 2:
            return self.getAllVectorsByCoupleClustersName(cluster_names_tuple[0], cluster_names_tuple[1])
        if combination_size == 3:
            couple_vec_lists = self.getAllVectorsByCoupleClustersName(cluster_names_tuple[0], cluster_names_tuple[1])
            single_vec_list = self.getAllVectorsBySingleClusterName(cluster_names_tuple[2])
            return findMatchVectors(couple_vec_lists, single_vec_list)
        print("you insert illegal combination")
        return None

    def makeCombinationsGroups(self):
        # generate data to the combinations step
        kmeans_names = [cluster_name for cluster_name in self.kmeans_clusters]
        spectral_names = [cluster_name for cluster_name in self.spectral_clusters]
        connected_names = [cluster_name for cluster_name, i in zip(self.connected_clusters, range(10))]
        triple = [kmeans_names, spectral_names, connected_names]
        double1 = [kmeans_names, spectral_names]
        double2 = [kmeans_names, connected_names]
        double3 = [connected_names, spectral_names]

        # generate all to possible combinations
        all_possible_combinations = list(itertools.product(*triple)) + list(itertools.product(*double1)) + \
                                    list(itertools.product(*double2)) + list(itertools.product(*double3))

        # generate all to valid combinations
        kmeans_names = [tuple([cluster_name]) for cluster_name in self.kmeans_clusters]
        spectral_names = [tuple([cluster_name]) for cluster_name in self.spectral_clusters]
        connected_names = [tuple([cluster_name]) for cluster_name in self.connected_clusters]
        valid_combinations = kmeans_names + spectral_names + connected_names

        for combination in all_possible_combinations:
           if self.getAllVectorsByCombinationClustersName(combination) is not None:
               valid_combinations.append(combination)

        return valid_combinations
