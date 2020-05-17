import matplotlib as matplotlib
from matplotlib import pylab
from mpl_toolkits.mplot3d import proj3d
from sklearn.cluster import KMeans as KMeansAlgorithm # Algorithm
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler

# matplotlib.use('MacOSX')

class KMeans:
    def __init__(self, vectors_3dim, color,arrow_size):
        self.vectors_3dim = vectors_3dim
        self.color = color
        self.km = KMeansAlgorithm(n_clusters=self.find_elbow(), init='k-means++', max_iter=300, n_init=10, random_state=0)
        self.km.fit_predict(self.vectors_3dim)
        self.arrow_size = arrow_size

    def find_elbow(self):
        mms = MinMaxScaler()
        mms.fit(self.vectors_3dim)
        data_transformed = mms.transform(self.vectors_3dim)

        Sum_of_squared_distances = []
        K = range(1, int(0.01*len(data_transformed)))
        for k in K:
            km = KMeansAlgorithm(n_clusters=k)
            km = km.fit(self.vectors_3dim)
            Sum_of_squared_distances.append(km.inertia_)
            if (len(Sum_of_squared_distances))>1:
                gradient = Sum_of_squared_distances[k-1] - Sum_of_squared_distances[k-2]
                if gradient > -1200:
                    return k-3

    def getPlot(self):

        # Create a scatter plot
        fig = plt.figure(dpi=120, figsize=(8.0, 5.0))
        ax = fig.add_subplot( 111, projection='3d')

        # drow all the nodes in the grapg
        ax.scatter(self.vectors_3dim[:, 0], self.vectors_3dim[:, 1], self.vectors_3dim[:, 2], s=1)

        # drow the clusters
        ax.scatter(self.km.cluster_centers_[:, 0], self.km.cluster_centers_[:, 1],
                            self.km.cluster_centers_[:, 2], s=700, c=self.color, marker = 'o', depthshade=False)

        # drow clusters label
        cluster_name = ["K" + str(i) for i in range(len(self.km.cluster_centers_))]
        for i, name in enumerate(cluster_name):
            x2, y2, _ = proj3d.proj_transform(self.km.cluster_centers_[i,0], self.km.cluster_centers_[i,1],self.km.cluster_centers_[i,2], ax.get_proj())

            label = pylab.annotate(
                name,
                xy=(x2, y2), xytext=(-1*self.arrow_size, -1*self.arrow_size),
                textcoords='offset points', ha='right', va='bottom',
                bbox=dict(boxstyle='round,pad=0.5', fc=self.color, alpha=0.5),
                arrowprops=dict(arrowstyle='->', connectionstyle='arc3,rad=0'))

            def update_position(e):
                x2, y2, _ = proj3d.proj_transform(1, 1, 1, ax.get_proj())
                label.xy = x2, y2
                label.update_positions(fig.canvas.renderer)
                fig.canvas.draw()

            fig.canvas.mpl_connect('button_release_event', update_position)


        # the axis labels
        ax.set_xlabel('X Label')
        ax.set_ylabel('Y Label')
        ax.set_zlabel('Z Label')
        return pylab

