import matplotlib as matplotlib
import matplotlib.pyplot as plt
matplotlib.use('MacOSX')

class SpectralClustering:
    def __init__(self, vectors_3dim, color):
        self.vectors_3dim = vectors_3dim
        self.color = color

    def getPlot(self):
        print(self.color)


