import matplotlib as matplotlib
from matplotlib import pylab
from mpl_toolkits.mplot3d import proj3d
from sklearn.cluster import KMeans as KMeansAlgorithm # Algorithm
import matplotlib.pyplot as plt
from sklearn.cluster import SpectralClustering as SpectralClusteringAlgorithm # Algorithm
from sklearn.preprocessing import MinMaxScaler

# matplotlib.use('MacOSX')


class Combined:
    def __init__(self, kmeans,spectral,connected):
        self.kmeans = kmeans
        self.spectral =spectral
        self.connected = connected

    def kmeansPlot(self,ax,fig):
        # drow kmeans clusters
        ax.scatter(self.kmeans.km.cluster_centers_[:, 0], self.kmeans.km.cluster_centers_[:, 1],
                   self.kmeans.km.cluster_centers_[:, 2], s=700, c=self.kmeans.color, marker='o', depthshade=False)

        # drow clusters label
        cluster_name = ["K" + str(i) for i in range(len(self.kmeans.km.cluster_centers_))]
        for i, name in enumerate(cluster_name):
            x2, y2, _ = proj3d.proj_transform(self.kmeans.km.cluster_centers_[i, 0], self.kmeans.km.cluster_centers_[i, 1],
                                              self.kmeans.km.cluster_centers_[i, 2], ax.get_proj())

            label = pylab.annotate(
                name,
                xy=(x2, y2), xytext=(-1*self.kmeans.arrow_size, -1*self.kmeans.arrow_size),
                textcoords='offset points', ha='right', va='bottom',
                bbox=dict(boxstyle='round,pad=0.5', fc=self.kmeans.color, alpha=0.5),
                arrowprops=dict(arrowstyle='->', connectionstyle='arc3,rad=0'))

            def update_position(e):
                x2, y2, _ = proj3d.proj_transform(1, 1, 1, ax.get_proj())
                label.xy = x2, y2
                label.update_positions(fig.canvas.renderer)
                fig.canvas.draw()

            fig.canvas.mpl_connect('button_release_event', update_position)

    def spectralPlot(self,ax,fig):
        # drow spectral clusters
        for i in range(len(self.spectral.CenterClusterList)):
            center = self.spectral.CenterClusterList[i]
            ax.scatter(center[0], center[1], center[2], c=self.spectral.color, marker='^', s=700, depthshade=False)

            # drow clusters label
            x2, y2, _ = proj3d.proj_transform(center[0], center[1], center[2], ax.get_proj())

            label = pylab.annotate(
                "S" + str(i),
                xy=(x2, y2), xytext=(self.spectral.arrow_size*1.4, self.spectral.arrow_size*0.6),
                textcoords='offset points', ha='right', va='bottom',
                bbox=dict(boxstyle='round,pad=0.5', fc=self.spectral.color, alpha=0.5),
                arrowprops=dict(arrowstyle='->', connectionstyle='arc3,rad=0'))

            def update_position(e):
                x2, y2, _ = proj3d.proj_transform(1, 1, 1, ax.get_proj())
                label.xy = x2, y2
                label.update_positions(fig.canvas.renderer)
                fig.canvas.draw()

            fig.canvas.mpl_connect('button_release_event', update_position)

    def connectedPlot(self,ax,fig):
        # drow connected clusters
        ax.scatter(
            xs=self.connected.component_centers[:, 0],
            ys=self.connected.component_centers[:, 1],
            zs=self.connected.component_centers[:, 2],
            s=self.connected.component_radiuses,
            c=self.connected.color,
            marker='s',
            depthshade=False)

        # drow clusters label
        cluster_name = ["C" + str(i) for i in range(min(len(self.connected.component_centers), 6))]
        for i, name in enumerate(cluster_name):
            x2, y2, _ = proj3d.proj_transform(self.connected.component_centers[i, 0], self.connected.component_centers[i, 1],
                                              self.connected.component_centers[i, 2], ax.get_proj())

            label = pylab.annotate(
                name,
                xy=(x2, y2), xytext=(0, -1*self.connected.arrow_size),
                textcoords='offset points', ha='right', va='bottom',
                bbox=dict(boxstyle='round,pad=0.5', fc=self.connected.color, alpha=0.5),
                arrowprops=dict(arrowstyle='->', connectionstyle='arc3,rad=0'))

            def update_position(e):
                x2, y2, _ = proj3d.proj_transform(1, 1, 1, ax.get_proj())
                label.xy = x2, y2
                label.update_positions(fig.canvas.renderer)
                fig.canvas.draw()

            fig.canvas.mpl_connect('button_release_event', update_position)

    def getPlot(self, mode):
        # Create a scatter plot
        fig = plt.figure(dpi=120, figsize=(8.0, 5.0))
        ax = fig.add_subplot( projection='3d')

        # drow all the nodes in the graph
        ax.scatter(self.kmeans.vectors_3dim[:, 0], self.kmeans.vectors_3dim[:, 1], self.kmeans.vectors_3dim[:, 2], s=1)

        if mode == "kmeans+spectral":
            # drow kmeans clusters
            self.kmeansPlot(ax,fig)
            # drow spectral clusters
            self.spectralPlot(ax,fig)

        elif mode == "kmeans+connected":
            # drow kmeans clusters
            self.kmeansPlot(ax,fig)
            # drow connected clusters
            self.connectedPlot(ax,fig)

        elif mode == "spectral+connected":
            # drow spectral clusters
            self.spectralPlot(ax.fig)
            # drow connected clusters
            self.connectedPlot(ax,fig)

        elif mode == "kmeans+spectral+connected":
            # drow kmeans clusters
            self.kmeansPlot(ax,fig)
            # drow spectral clusters
            self.spectralPlot(ax,fig)
            # drow connected clusters
            self.connectedPlot(ax,fig)

            # the axis labels
            ax.set_xlabel('X Label')
            ax.set_ylabel('Y Label')
            ax.set_zlabel('Z Label')
        return pylab

