import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import pylab
from mpl_toolkits.mplot3d import proj3d
from sklearn.preprocessing import MinMaxScaler

np.set_printoptions(threshold=np.inf)
SIZE = 160
MAX_CLUSTERS_ANOUNT = 8
# matplotlib.use('MacOSX')

def ConnectedComponents_center(set_3dim_vec):
    center = np.array([0,0,0])
    for vec in set_3dim_vec:
        center = center + np.array(vec)

    return center/len(set_3dim_vec)

def ConnectedComponents_center_radius(set_3dim_vec):
    center = ConnectedComponents_center(set_3dim_vec)
    max_dist =np.array([0,0,0])
    for vec in set_3dim_vec:
        dist = abs(np.array(vec)-center)
        for i in range(3):
            max_dist[i] = max(max_dist[i],dist[i])
    return (center,max(max_dist[0],max_dist[1],max_dist[2])/2)

def make_vec3D_connected_components(G, vectors_3dim):
    # makeDictionary_Id_vector
    id2vec_dic = {}
    for id, vec in zip(G.nodes(),vectors_3dim):
        id2vec_dic[id] = vec
    vec3D_connected_components = []
    for group in list(nx.connected_components(G)):
        vec3D_group = []
        for id in group:
            vec3D_group.append(id2vec_dic[id])
        vec3D_connected_components.append(vec3D_group)
    return vec3D_connected_components



class ConnectedComponents:
    def __init__(self, vectors_3dim, G, color, arrow_size):
        sets_vectors_3dim = make_vec3D_connected_components(G, vectors_3dim)
        self.sets_vectors_3dim = sets_vectors_3dim
        self.vectors_3dim = vectors_3dim
        self.color = color
        self.component_centers = []
        self.component_radiuses = []
        for vectors_set in self.sets_vectors_3dim:
            (center, radius) = ConnectedComponents_center_radius(vectors_set)
            self.component_centers.append(center)
            self.component_radiuses.append(radius)

        self.component_centers = np.array(self.component_centers)
        self.component_radiuses = np.array(self.component_radiuses) * SIZE
        self.arrow_size = arrow_size

    def getPlot(self):
        # Create a scatter plot
        fig = plt.figure(dpi=120, figsize=(8.0, 5.0))
        ax = fig.add_subplot(projection='3d')

        #drow all the nodes in the grapg
        ax.scatter(self.vectors_3dim[:, 0], self.vectors_3dim[:, 1], self.vectors_3dim[:, 2], s=1, alpha=0.1)

        # drow the clusters and labels
        for name, vector in self.clustersNames().items():
            #clusters
            ax.scatter(vector[0], vector[1], vector[2],
                       s=600, c=self.color, marker='s', depthshade=False, alpha=0.2)
            #labels
            ax.text(vector[0] - 0.3, vector[1] - 0.3, vector[2] - 0.3, name, None)

        #the axis labels
        ax.set_xlabel('X Label')
        ax.set_ylabel('Y Label')
        ax.set_zlabel('Z Label')

        return plt

    # Get dictionary of centers by cluster name
    def clustersNames(self):
        connected_centers_name = {}
        for i, center in enumerate(self.component_centers):
            if i < MAX_CLUSTERS_ANOUNT:
                connected_centers_name["C" + str(i)] = center
        return connected_centers_name


