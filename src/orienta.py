import numpy as np
import scipy
import matplotlib.pyplot as plt
from mylib.convolucao import *
from scipy import stats
from mylib.saveDataBase import *

#from skimage import data
#from skimage.util import img_as_float
#from skimage.filters import gabor_kernel

def getSobelMapGxGy(img, operador, i, j):
    valorGw = 0

    for ii in range(0, len(img)):
        for jj in range(0, len(img[0])):
            valorGw += operador[ii][jj] * img[ii][jj]

    return valorGw

"""
__GLOBAL_VARS__
"""
mapa   = []
mapaGx = []
mapaGy = []
mapaTheta  = []
gsOperator = initMatrix(7, 7, 1)
sobelGy = [(-1, -2, -1),
           ( 0,  0,  0),
           ( 1,  2,  1)]

sobelGx = [(-1,  0,  1),
           (-2,  0,  2),
           (-1,  0,  1)]

"""
__MAIN__
"""
nomeImg = "img*/" + sys.argv[2]
tipoImg = sys.argv[1]
opc     = sys.argv[3]
nome    = ''
if(opc == 'salvar'):
    nome = sys.argv[4]

Img     = scipy.misc.imread(nomeImg + "." + tipoImg)
Img2    = plt.imread(nomeImg.replace('*', '') + "." + tipoImg)

mapaGy    = convoluir(Img, sobelGy, getSobelMapGxGy)
mapaGx    = convoluir(Img, sobelGx, getSobelMapGxGy)
t = 8
mapaTheta = initMatrix(Img.shape[1]/t, Img.shape[0]/t, -1)

print '->Gerando mapa de Orientacoes'
for i in range(0, len(Img), t):
    for j in range(0, len(Img[0]), t):
        sumGsy = 0
        sumGsx = 1
        vet = []
        for ii in range(0, t):
            for jj in range(0, t):
                sumGsy += 2 * mapaGx[ii+i][jj+j] * mapaGy[ii+i][jj+j]
                sumGsx += pow(mapaGx[ii+i][jj+j], 2) - pow(mapaGy[ii+i][jj+j], 2)
                vet.append(Img[ii+i][jj+j])

        if(math.sqrt(np.var(vet)) > 30):
            phi = 0.5 * np.arctan2(sumGsy, sumGsx)
            k   = 0
            if(phi < 0 and sumGsy < 0) or (phi >= 0 and sumGsy > 0):
                k = 0.5
            elif(phi < 0 and sumGsy >= 0):
                k = 1.0
            elif(phi >= 0 and sumGsy <= 0):
                k = 0
            theta = np.rad2deg(phi + k*math.pi)

            if(theta > 0 and theta < 45):
                theta -= (theta)*2
            elif(theta > 45 and theta < 90):
                theta += (90 - theta)*2
            elif(theta > 90 and theta < 135):
                theta -= (theta - 90)*2
            elif(theta > 135 and theta < 180):
                theta += (180 - theta)*2
            elif(theta > 180 and theta < 225):
                theta -= (theta - 180)*2
            elif(theta > 225 and theta < 270):
                theta += (270 - theta)*2
            elif(theta >270 and theta < 315):
                theta -= (theta - 270)*2
            elif(theta > 315 and theta < 360):
                theta += (360 - theta)*2
            mapaTheta[i/8][j/8] = theta

            if(opc == 'salvar'):
                plot_point((j, i), theta, 3)

if(opc == 'salvar'):
    print '->Salvando info em BD'
    salvarBanco(nome, mapaTheta)
    plt.imshow(Img2, alpha = 0.5)
    plt.show()
else:
    print '->Buscando digital em BD'
    buscarBanco(mapaTheta)

print 'OK!'
