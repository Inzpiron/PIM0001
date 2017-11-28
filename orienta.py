import numpy as np
import scipy
import matplotlib.pyplot as plt
from mylib.convolucao import *
from scipy import stats

from skimage import data
from skimage.util import img_as_float
from skimage.filters import gabor_kernel

def angle_between(p1, p2):
    ang1 = np.arctan2(*p1[::-1])
    ang2 = np.arctan2(*p2[::-1])
    return np.rad2deg((ang1 - ang2) % (2 * np.pi))

def getAngleBySobel(img, operador, i, j):
    valorGx = 0
    valorGy = 0
    for i in range(0, len(img)):
        for j in range(0, len(img[0])):
            valorGx += sobelGx[i][j] * img[i][j]
            valorGy += sobelGy[i][j] * img[i][j]

    ang = int(round(angle_between((0, 0), (valorGy, valorGx))))

    return ang

def segmentaBySobel(img, operator, i, j):
    operator = getOperatorFromAngle(mapa[i][j])
    #if(mapa[i][j] == 45 or mapa[i][j] == 225):
    #    return 255
    valor = 0
    for i in range(0, len(img)):
        for j in range(0, len(img[0])):
            valor += operator[i][j] * img[i][j]

    valor = normaliza255(valor)
    return valor

"""
__GLOBAL_VARS__
"""
mapa    = []

sobelD1 = [(-1, -2,  0),
           (-2,  0,  2),
           ( 0,  2,  1)]

sobelD2 = [( 0,  2,  1),
           (-2,  0,  2),
           (-1, -2,  0)]

sobelGx = [(-1, -2, -1),
           ( 0,  0,  0),
           ( 1,  2,  1)]

sobelGy = [(-1,  0,  1),
           (-2,  0,  2),
           (-1,  0,  1)]

"""
__MAIN__
"""
nomeImg = "img/" + sys.argv[2]
tipoImg = sys.argv[1]
img     = scipy.misc.imread(nomeImg + "." + tipoImg)
img2    = plt.imread(nomeImg.replace('*', '') + "." + tipoImg)



mapa    = convoluir(img, sobelGx, getAngleBySobel)
t       = 8


vetDotX = []
vetDotY = []
for i in range(0, len(mapa), t):
    for j in range(0, len(mapa[0]), t):
        vet = []
        for k in range(0, t):
            for l in range(0, t):
                vet.append(mapa[i+k][j+l])

        #valor = scipy.stats.mode(vet)[0][0]
        valor = np.average(vet)#scipy.stats.average(vet)#[0][0]

        for k in range(0, t):
            for l in range(0, t):
                mapa[i+k][j+l] = valor

        if(i > 10 and i < img.shape[0] - 10 and j > 10 and j < img.shape[1]-10):
            plot_point((j, i), mapa[i][j], 5)


print "a"
plt.imshow(img2)
plt.show()

#data = convoluir(img, sobelGx, segmentaBySobel)
#scipy.misc.imsave(nomeImg + "*." + tipoImg, data)
'''
imgGx = convoluir(img, sobelGx, sobel)
#imgGy = convoluir(img, sobelGy, sobel)
scipy.misc.imsave(nomeImg + "*Gx." + tipoImg, imgGx)
#scipy.misc.imsave(nomeImg + "*Gy." + tipoImg, imgGy)
'''
