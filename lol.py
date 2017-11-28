import matplotlib.pyplot as plt
import itertools
import numpy as np
import math


def plot_point(point, angle, length):
     '''
     point - Tuple (x, y)
     angle - Angle you want your end point at in degrees.
     length - Length of the line you want to plot.

     Will plot the line on a 10 x 10 plot.
     '''

     # unpack the first point
     x, y = point
     angle -= 90
     # find the end point
     x1  = length * np.sin(np.deg2rad(angle))
     y1  = length * np.cos(np.deg2rad(angle))
     x1 = int(x1)
     y1 = int(y1)

     print x, y
     print x + x1, y + y1
     plt.plot([x, x + x1], [y, y + y1], 'C3')
     plt.plot([x, x - x1], [y, y - y1], 'C3')


img = plt.imread("img/digital.jpg")
plot_point((147, 200), ang, 3)
plt.imshow(img)
plt.show()
