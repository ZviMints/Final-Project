import matplotlib as matplotlib
import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
from sklearn.cluster import linkage_tree # Algorithm
from sklearn.cluster import AgglomerativeClustering # Algorithm
from sklearn.cluster import AffinityPropagation # Algorithm
from sklearn.decomposition import PCA  # From 64dim to 3dim
from sklearn.preprocessing import StandardScaler, RobustScaler, Normalizer  # Normalized
import pandas as pd

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

class ConnectedComponents:
    def __init__(self, sets_vectors_3dim, df, color):
        self.sets_vectors_3dim = sets_vectors_3dim
        self.df = df
        self.color = color

    def getPlot(self):
        component_centers = []
        component_radiuses = []
        for vectors_set in self.sets_vectors_3dim:
            (center,radius) = ConnectedComponents_center_radius(vectors_set)
            component_centers.append(center)
            component_radiuses.append(radius)

        component_centers = np.array(component_centers)
        component_radiuses = np.array(component_radiuses)*100

        # Create a scatter plot
        base_figure = plt.figure(dpi=120, figsize=(160, 100)).gca(projection='3d')
        base_figure.scatter(
            xs=self.df["pca-one"],
            ys=self.df["pca-two"],
            zs=self.df["pca-three"],
            s=1
        )

        base_figure.scatter(
            xs=component_centers[:,0],
            ys=component_centers[:,1],
            zs=component_centers[:,2],
            depthshade=False,
            s=1000,
            c=self.color
        )

        base_figure.set_xlabel('x axis')
        base_figure.set_ylabel('y axis')
        base_figure.set_zlabel('z axis')

        return plt

