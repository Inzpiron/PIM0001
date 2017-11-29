import numpy as np
import scipy
import matplotlib.pyplot as plt
from mylib.convolucao import *
from scipy import stats

from skimage import data
from skimage.util import img_as_float
from skimage.filters import gabor_kernel

def getSobelMapGxGy(img, operador, i, j):
    valorGw = 0

    for ii in range(0, len(img)):
        for jj in range(0, len(img[0])):
            valorGw += operador[ii][jj] * img[ii][jj]

    return valorGw

def getOrientationBySobel(img, operador, i, j):
    sumGsy = 0
    sumGsx = 0
    for ii in range(0, len(img)):
        for jj in range(0, len(img[0])):
            sumGsy += 2*mapaGx[ii+i][jj+j]*mapaGy[ii+i][jj+j]
            sumGsx += pow(mapaGx[ii+i][jj+j], 2) - pow(mapaGy[ii+i][jj+j], 2)

    if(sumGsx == 0):
        sumGsx = 1

    print np.matrix(img)
    print sumGsx
    print sumGsy
    phi = 1/2 * np.arctan2(sumGsy,sumGsx)
    k   = 0
    if(phi < 0 and sumGsy < 0) or (phi >= 0 and sumGsy > 0):
        k = 1/2
    elif(phi < 0 and sumGsy >= 0):
        k = 1
    elif(phi >= 0 and sumGsy <= 0):
        k = 0

    theta = phi + k*math.pi
    print theta
    raw_input()
    return theta

"""
__GLOBAL_VARS__
"""
mapa   = []
mapaGx = []
mapaGy = []
mapaTheta  = []
gsOperator = initMatrix(9, 9, 1)
sobelGy = [(-1, -2, -1),
           ( 0,  0,  0),
           ( 1,  2,  1)]

sobelGx = [(-1,  0,  1),
           (-2,  0,  2),
           (-1,  0,  1)]

"""
__MAIN__
"""
nomeImg = "img/" + sys.argv[2]
tipoImg = sys.argv[1]
img     = scipy.misc.imread(nomeImg + "." + tipoImg)
img2    = plt.imread(nomeImg.replace('*', '') + "." + tipoImg)

mapaGy    = convoluir(img, sobelGy, getSobelMapGxGy)
mapaGx    = convoluir(img, sobelGx, getSobelMapGxGy)
mapaTheta = convoluir(img, gsOperator, getOrientationBySobel)

print "GO"


'''
t = 8
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
                if(mapa[i+k][j+l] != -1 and mapa[i+k][j+l] != 90 and mapa[i+k][j+l] != 180):
                    plot_point((j+l, i+k), mapa[i+k][j+l], 2)

                mapa[i+k][j+l] = valor
plt.imshow(img2)
plt.show()
'''

#data = convoluir(img, sobelGx, segmentaBySobel)
#scipy.misc.imsave(nomeImg + "*." + tipoImg, data)
'''
imgGx = convoluir(img, sobelGx, sobel)
#imgGy = convoluir(img, sobelGy, sobel)
scipy.misc.imsave(nomeImg + "*Gx." + tipoImg, imgGx)
#scipy.misc.imsave(nomeImg + "*Gy." + tipoImg, imgGy)
'''
