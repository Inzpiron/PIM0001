import numpy as np
import matplotlib.pyplot as plt
import scipy.misc
import sys
import os
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

     #print x, y
     #print x + x1, y + y1
     plt.plot([x, x + x1], [y, y + y1], 'C3')
     plt.plot([x, x - x1], [y, y - y1], 'C3')

def angle_between(p1, p2):
    ang1 = np.arctan2(*p1[::-1])
    ang2 = np.arctan2(*p2[::-1])
    return np.rad2deg((ang1 - ang2) % (2 * np.pi))

def normaliza255(valor):
    valor = min([valor, 255])
    valor = max([0,   valor])
    return valor

def somaMatriz(m1, m2):
    data = []
    for i in range(0, len(m1)):
        row = []
        for j in range(0, len(m1[0])):
            valor = m1[i][j] + m2[i][data.append(row)]
            valor = min([valor, 255])
            valor = max([0,   valor])
            row.append(valor)
        data.append(row)

    return data

def getDxDy(t):
    dy = []
    for i in range(-int(math.floor(t/2.0)), int(math.floor(t/2.0)+1)):
        for j in range(0, t):
            dy.append(i)

    dx = []
    for i in range(0, t):
        for j in range(-int(math.floor(t/2.0)), int(math.floor(t/2.0)+1)):
            dx.append(j)

    return (dy, dx)

def convoluir(img, operator, funcValor):
    data = []
    sizey = len(img)
    sizex = len(img[0])

    for i in range(0, sizey):
        row = []
        for j in range(0, sizex):
            dy,dx = getDxDy(len(operator))
            mapa  = [[255 for ii in range(len(operator))] for jj in range(len(operator[0]))]
            t     = int(math.floor(len(operator)/2.0))

            for k in range(0, len(dx)):
                if(i+dy[k] < sizey and i+dy[k] >= 0 and j+dx[k] < sizex and j+dx[k] >= 0):
                    mapa[dy[k]+t][dx[k]+t] = img[i+dy[k]][j+dx[k]]

            valor = funcValor(mapa, operator, i, j)

            row.append(valor)
        data.append(row)
    return data
