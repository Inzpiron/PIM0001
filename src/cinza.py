import numpy as np
import matplotlib.pyplot as plt
import scipy.misc
import sys
import os

nomeImg = "img/" + sys.argv[2]
tipoImg = sys.argv[1]
img  = scipy.misc.imread(nomeImg + "." + tipoImg)
nomeImg = nomeImg.replace('img','img*')
data = []

print '->Gerando a imagem em tons de cinza'
for i in range(0, img.shape[0]):
	row = []
	for j in range(0, img.shape[1]):
		color = 0.299*img[i][j][0] + 0.587*img[i][j][1] + 0.114*img[i][j][2]
		color = int(round(color))
		row.append(color);

	data.append(row)

scipy.misc.imsave(nomeImg + "."+ tipoImg, data)
print 'OK!'
