import numpy as np
import subprocess as sp
import sys

#!pip install graphlib
def install(graphlib):
    sp.check_call([sys.executable, "-m", "pip", "install", graphlib])

class Vertice(object):
    def __init__(self, pos, arestas, custo):
        self.pos = pos
        self.custo = custo #Número da matriz
        self.arestas = arestas
        self.ultimoNoVisitado = None
        self.custoTotal = None


class Graph(object):
    def __init__(self, matriz, shape):
        self.custoTotal = 0
        self.posicaoAnterior = None
        self.mapa = matriz
        self.vertices = []
        for i in range(shape[0]):
            for j in range(shape[0]):
                try:
                    self.vertices.append([i+1, j]) # Sul
                except:
                    None
                try:
                    self.vertices.append([i-1, j]) # Norte
                except:
                    None
                try:
                    self.vertices.append([i, j+1]) # Leste
                except:
                    None
                try:
                    self.vertices.append([i, j-1]) # Oeste
                except:
                    None

                self.vertices.append(Vertice([i, j], self.vertices, self.mapa[i][j]))

    def getVertices(self):
        return self.vertices

    def setCustoTotal(self, custo):
        self.custoTotal = custo

    def getNo(self, posicao):
        return self

    def getCusto(self, posicao):
        return self.custo

    def getPosicaoAnterior(self):
        return self.posicaoAnterior

mat = np.array([[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]])

mat.shape

grafo = Graph(mat, mat.shape)

print(grafo.getVertices())

