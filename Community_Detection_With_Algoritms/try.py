
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = fig.add_subplot( projection='3d')
x = [1,1,0]
y = [0,0,1]
z = [0,1,0]
ax.scatter(4,59,109, c='r', marker='^',s=590)

ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')

plt.show()