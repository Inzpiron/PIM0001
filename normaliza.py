import sys
import numpy as np
import matplotlib.pyplot as plt
import scipy.misc
import os
import math
from mylib.convolucao import *

def initMatrix(nl, nc, value):
    mapa = [[value for ii in range(len(nl))] for jj in range(nc))]
    return mapa

def imgMedia(img):
    result = 0
    for i in range(0, len(img)):
        for j in range(0, len(img[0])):
            result += img[i][j]

    result = result/(len(img) * len(img[0]) * 1.0)
    return result

def imgVariancia(img):
    result = 0
    media = imgMedia(img)
    for i in range(0, len(img)):
        for j in range(0, len(img[0])):
            result += pow((img[i][j]-media), 2)

    result = result/(len(img) * len(img[0]))
    return result

def filtroVariancia(img, media, var, i, j):
    m0   = 100.0
    var0 = 100.0

    data = []
    for i in range(0, len(img)):
        row = []
        for j in range(0, len(img[0])):
            if(img[i][j] > media):
                valor = m0 + np.sqrt((var0 * pow((img[i][j]-media), 2))/var)
            else:
                valor = m0 - math.sqrt((var0 * pow((img[i][j]-media), 2))/var)

            print str(img[i][j]) + ','#, valor
            #raw_input()
            valor = int(round(valor))
            #print valor
            row.append(valor)
        data.append(row)

    return data


def filtroContraste(mapa, operator, i, j):
    valor = 0
    for i in range(0, len(mapa)):
        for j in range(0, len(mapa[0])):
            if(mapa[i][j] != -1):
                valor += operator[i][j] * mapa[i][j]
    valor = valor/3
    valor = min([valor, 255])
    valor = max([0,   valor])
    return valor

def filtroMediana(mapa, operator, i, j):
    vet = []
    for i in range(0, len(mapa)):
        for j in range(0, len(mapa[0])):
            if(mapa[i][j] != -1):
                vet.append(mapa[i][j])

    return int(np.median(vet))

operator = [(-1,-1,-1,-1,-1),
            (-1, 2, 2, 2,-1),
            (-1, 2, 3, 2,-1),
            (-1, 2, 2, 2,-1),
            (-1,-1,-1,-1,-1)]

operator1 = [(1, 1, 1),
             (1, 1, 1),
             (1, 1, 1)]


nomeImg = "img/" + sys.argv[2]
tipoImg = sys.argv[1]
img     = scipy.misc.imread(nomeImg + "." + tipoImg)
'''
process(img)
#data0 = convoluir(img, operator, filtroContraste)
media = imgMedia(img)
variancia = imgVariancia(img)
print media, variancia
data1 = filtroVariancia(img, media, variancia)
scipy.misc.imsave(nomeImg + "lol." + tipoImg, data1)
'''

print "Filtro contraste"
data0 = convoluir(img, operator, filtroContraste)
print "Filtro mediana"
data1 = convoluir(data0, operator1, filtroMediana)
scipy.misc.imsave(nomeImg + "*." + tipoImg, data1)
