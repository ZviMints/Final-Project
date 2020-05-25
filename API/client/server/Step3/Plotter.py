from sklearn import decomposition
from sklearn.preprocessing import StandardScaler
#windows import
# from Step3.algorithms import KMeans, BaseGraph, \
#     ConnectedComponents, SpectralClustering, Combined
#linux imports
import sys
sys.path.append('/mnt/c/Users/EILON/PycharmProjects/Final-Project/Step3/algorithms/')
import KMeans, BaseGraph, ConnectedComponents, SpectralClustering, Combined
# matplotlib.use('MacOSX')

# =============================================== Help Methods ===============================================
def make_PCA(G, model):
    pca = decomposition.PCA(n_components=3)
    # all_vectors_after_pca = pca.fit_transform(StandardScaler().fit_transform(model.vectors))
    all_vectors_after_pca = pca.fit_transform(StandardScaler().fit_transform(model.vectors))
    return all_vectors_after_pca

# =============================================== Plotter ===============================================
# This class is responsible to plot
# He has algorithms and functions
class Plotter:

    # G is networkx
    # model is after node2vec embedded
    def __init__(self, G, model):
        self.all_vectors_after_pca = make_PCA(G, model)

        # Make base graph (without algorithm)
        self.BaseGraph = BaseGraph.BaseGraph(self.all_vectors_after_pca)

        # Make Kmeans
        self.kmeans = KMeans.KMeans(self.all_vectors_after_pca, "red", 20)

        # Make Connected Componenet
        self.cc = ConnectedComponents.ConnectedComponents(self.all_vectors_after_pca, G, "green", 40)

        # Make Spectral
        self.spectral = SpectralClustering.SpectralClustering(self.all_vectors_after_pca, "yellow", 20)

        #Make Combined
        self.Combined = Combined.Combined( self.kmeans,self.spectral,self.cc)

    # Plotting the Graph with no algo
    def showWithBaseGraph(self):
        self.BaseGraph.getPlot().show()

    # Plotting the Graph with KMeans
    def showWithKMeans(self):
        self.kmeans.getPlot().show()

    # Plotting the Graph with ConnectedComponents
    def showWithCC(self):
        self.cc.getPlot().show()

    # Plotting the Graph with SpectralClustering
    def showWithSpectral(self):
        self.spectral.getPlot().show()

    def showCombined(self, mode):
        self.Combined.getPlot(mode).show()

    def getAll(self):
        algorithms = {}
        algorithms["base"] = self.BaseGraph.getPlot()
        algorithms["kmeans"] = self.kmeans.getPlot()
        algorithms["spectral"] = self.spectral.getPlot()
        algorithms["connected"] = self.cc.getPlot()
        algorithms["kmeans+spectral"] = self.Combined.getPlot("kmeans+spectral")
        algorithms["connected+kmeans"] = self.Combined.getPlot("kmeans+connected")
        algorithms["connected+spectral"] = self.Combined.getPlot("spectral+connected")
        algorithms["connected+kmeans+spectral"] = self.Combined.getPlot("kmeans+spectral+connected")
        return algorithms

    def SaveAll(self,prefix):
        self.BaseGraph.getPlot().savefig("." + prefix + "/base.png")
        self.kmeans.getPlot().savefig("." + prefix + "/kmeans.png")
        self.spectral.getPlot().savefig("." + prefix + "/spectral.png")
        self.cc.getPlot().savefig("." + prefix + "/connected.png")
        self.Combined.getPlot("kmeans+spectral").savefig("." + prefix + "/kmeans+spectral.png")
        self.Combined.getPlot("kmeans+connected").savefig("." + prefix + "/connected+kmeans.png")
        self.Combined.getPlot("spectral+connected").savefig("." + prefix + "/connected+spectral.png")
        self.BaseGraph.getPlot().savefig("." + prefix + "/base.png")
        self.Combined.getPlot("kmeans+spectral+connected").savefig("." + prefix + "/connected+kmeans+spectral.png")

    def getAllCentersName(self):
        (kmeans_centers, spectral_centers, connected_center) = (self.kmeans.km.cluster_centers_,self.spectral.CenterClusterList,self.cc.component_centers)
        kmeans_centers_name = {}
        for i,center in enumerate(kmeans_centers):
            kmeans_centers_name["K"+str(i)] = center

        spectral_centers_name = {}
        for i, center in enumerate(spectral_centers):
            spectral_centers_name["S" + str(i)] = center

        connected_centers_name = {}
        for i, center in enumerate(connected_center):
            connected_centers_name["C" + str(i)] = center

        return (kmeans_centers_name, spectral_centers_name, connected_centers_name)
