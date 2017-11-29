import math
import numpy
import numpy as np
import scipy
import matplotlib.pyplot as plt
from mylib.convolucao import *
from scipy import ndimage

def sobel(mapa, operator):
    valorGx = 0
    valorGy = 0
    for i in range(0, len(mapa)):
        for j in range(0, len(mapa[0])):
            valorGx += sobelGx[i][j] * mapa[i][j]
            valorGy += sobelGy[i][j] * mapa[i][j]

    valor = math.sqrt(pow(normaliza255(valorGx),2) + pow(normaliza255(valorGy), 2))
    return int(round(valor))

"""
__GLOBAL_VARS__
"""

sobelGx = [(-1, -2, -1),
           ( 0,  0,  0),
           ( 1,  2,  1)]

sobelGy = [(-1, 0, 1),
           (-2, 0, 2),
           (-1, 0, 1)]
"""
__MAIN__
"""
nomeImg = "img/" + sys.argv[2]
tipoImg = sys.argv[1]
img  = scipy.misc.imread(nomeImg + "." + tipoImg)

imgGx = convoluir(img, sobelGx, sobel)
scipy.misc.imsave(nomeImg + "*." + tipoImg, imgGx)
