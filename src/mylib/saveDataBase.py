import numpy as np
from operator import itemgetter

def salvarBanco(nome, mapa):
    arq = open('dataBase.txt', 'a+')
    quad = []
    for i in [0, len(mapa)/2]:
        for j in [0, len(mapa[0])/2]:
            vet = []
            for ii in range(0, len(mapa)/2):
                for jj in range(0, len(mapa[0])/2):
                    if(mapa[i+ii][j+jj] != -1):
                        vet.append(mapa[i+ii][j+jj])
            quad.append(np.average(vet))

    texto = []
    texto.append(nome + ',')
    texto.append(str(quad[0]) + ',' + str(quad[1]) + ',' + str(quad[2]) + ',' + str(quad[3]) + '\n')
    arq.writelines(texto)
    arq.close()

def buscarBanco(mapa):
    quad = []
    for i in [0, len(mapa)/2]:
        for j in [0, len(mapa[0])/2]:
            vet = []
            for ii in range(0, len(mapa)/2):
                for jj in range(0, len(mapa[0])/2):
                    if(mapa[i+ii][j+jj] != -1):
                        vet.append(mapa[i+ii][j+jj])
            quad.append(np.average(vet))

    arq = open('dataBase.txt', 'r')
    info  = []
    maior = 0
    for line in arq.readlines():
        line = line.replace('\n', '').split(',')

        aux = 0
        for i in range(0, len(quad)):
            aux += abs(quad[i] - float(line[i+1]))

        info.append((line[0], aux))

        if(len(line[0]) > maior):
            maior = len(line[0])

    info.sort(key=itemgetter(1))
    for nome in info:
        print '{:>10}: {:<5} graus'.format(nome[0], nome[1])
