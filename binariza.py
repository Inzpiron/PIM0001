import numpy as np
import matplotlib.pyplot as plt
import scipy.misc
import sys
import os

nomeImg = "img/" + sys.argv[2]
tipoImg = sys.argv[1]
img  = scipy.misc.imread(nomeImg + "." + tipoImg)
nomeImg = nomeImg.replace("_2", "_3")

data = []
for i in range(0, img.shape[0]):
	row = []
	for j in range(0, img.shape[1]):
		if(img[i][j] < 160):
			row.append(0)
		else:
			row.append(255)
	data.append(row)

scipy.misc.imsave(nomeImg + "*."+ tipoImg, data)
