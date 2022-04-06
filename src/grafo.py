#from file import mapa
#import numpy as np
from front import *
import subprocess as sp
import sys

#!pip install graphlib
#def install(graphlib):
#    sp.check_call([sys.executable, "-m", "pip", "install", graphlib])

class Vertice(object):
    def __init__(self, pos, arestas, custo):
        self.pos = pos #lista com x e y
        if custo == 1:
            self.custo = custo
        elif custo == 2:
            self.custo = 5
        elif custo == 3:
            self.custo = 10
        elif custo == 4:
            self.custo = 15
        self.arestas = arestas #lista de vizinhos
        self.posicaoAnterior = None
        self.custoTotal = None

    def setCustoTotal(self, custo):
        self.custoTotal = custo

    def setPosicaoAnterior(self, posicao):
        self.posicaoAnterior = posicao

    def getArestas(self):
        return self.arestas

    def getCusto(self):
        return self.custo

    def getCustoTotal(self):
        return self.custoTotal

    def getPosicaoAnterior(self):
        return self.posicaoAnterior

    def getPosicao(self):
        return self.pos

    def __repr__(self):
        return str(self)

    def __str__(self):
        return str(self.__class__) + ": " + str(self.__dict__)


class Graph(object):
    def __init__(self, matriz, shape):
        self.vertices = []
        self.linha = matriz.shape[0]
        self.coluna = matriz.shape[1]
        gapw = 600 //  self.linha
        gaph = 600 //  self.coluna
        for i in range(shape[0]):
            for j in range(shape[1]):
                arestas = []
                if i-1 >= 0:
                    arestas.append([i-1, j]) # Norte
                if j+1 <= range(shape[1])[-1]:
                    arestas.append([i, j+1]) # Leste
                if i+1 <= range(shape[0])[-1]:
                    arestas.append([i+1, j]) # Sul
                if j-1 >= 0:
                    arestas.append([i, j-1]) # Oeste
                self.vertices.append(Spot(gaph , gapw, self.linha, self.coluna,[i,j],arestas,matriz[i][j]))

    def getVertices(self):
        return self.vertices

    def __repr__(self):
        return str(self)

    def setCustoTotal(self, posicao, custo):
        self.vertices[posicao[0] * self.coluna + posicao[1]].setCustoTotal(custo)

    def setPosicaoAnterior(self, posicao, anterior):
        self.vertices[posicao[0] * self.coluna + posicao[1]].setPosicaoAnterior(anterior)

    def getArestas(self, posicao):
        return self.vertices[posicao[0] * self.coluna + posicao[1]].getArestas()

    def getCustoTotal(self, posicao):
        if posicao == 0:
            return 0
        return self.vertices[posicao[0] * self.coluna + posicao[1]].getCustoTotal()

    def getCusto(self, posicao):
        return self.vertices[posicao[0] * self.coluna + posicao[1]].getCusto()

    def getPosicaoAnterior(self, posicao):
        if posicao == 0:
            return 0
        return self.vertices[posicao[0] * self.coluna + posicao[1]].getPosicaoAnterior()

#mat = np.array([[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]])
#mat.shape

#grafo = Graph(mapa, mapa.shape)

#print(grafo.__dict__)
#print(grafo.getVertices())

