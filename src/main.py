from file import *
from grafo import *
from front import *
import queue
import pandas as pd
import numpy as np
np.set_printoptions(threshold=np.inf)

"""
inicializa grafo
seta posição inicial na fila (coloca os valores certos nos atributos na posição inicial do grafo)
BFS(dequeue())
"""
def preparacaoBFS():
    fila.put(inicial) # @FRONT -> mudar a cor para posição inicial
    grafo.setPosicaoAnterior(inicial, 0)
    BFS(fila.get())

"""
noAtual = matriz[posAtual[0],posAtual[1]]
@FRONT -> mudar de cor o noAtual

Custo total = noAnterior.custoTotal + custo nó atual

Verifica se é o nó destino
    Se for, chama uma função para retornar o caminho
    @FRONT -> fazendo isso no retorno da recursão
    Ao retornar da função, exibe o custo total
    retorna

Insere as posições adjacentes na fila (N,L,S,O)
    Verifica se nó adjacente já foi ou será visitado (ant != NONE)
        noAdjacente.noAnterior = noAtual
        Adiciona na fila
        @FRONT -> muda de cor os nós adicionados na fila (a serem visitados)
BFS(fila.get(),noAtual)
retorna
"""
def BFS(posAtual):
    if posAtual == queue.Empty:
        return
    grafo.setCustoTotal(posAtual, grafo.getCustoTotal(grafo.getPosicaoAnterior(posAtual)) + grafo.getCusto(posAtual))
    if posAtual == final:
        print("Caminho encontrado (destino->início):")
        #print(grafo.__dict__)
        exibeCaminho(posAtual)
        print("\nCusto total:", grafo.getCustoTotal(posAtual))
        return
    for vertice in grafo.getArestas(posAtual):
        if grafo.getPosicaoAnterior(vertice) == None:
            grafo.setPosicaoAnterior(vertice, posAtual)
            fila.put(vertice)
    BFS(fila.get(block=False))
    #return

# @FRONT
# Função que exibe o caminho encontrado
def exibeCaminho(posicao):
    if posicao == 0:
        return
    print(posicao, end="")
    ##caminho.append(posicao)
    # Muda a cor da célula, exibindo o caminho
    # Recursão chamando noAnterior
    exibeCaminho(grafo.getPosicaoAnterior(posicao))

# MAIN
path = OpenFile()
if path != '':
    #print("path: \n", path)
    matriz = pd.read_csv(path, header = None).fillna(-1).to_numpy(dtype=int)
    inicial = [matriz[0][0], matriz[0][1]]
    final = [matriz[1][0], matriz[1][1]]
    mapa = np.delete(matriz,[0,1],0)
    rows, columns = mapa.shape
    if CoordTest(inicial, rows, columns) == True and CoordTest(final,rows,columns) == True and MapCheck(mapa) == True and inicial != final:
        #print("\npos inicial:\n ", inicial)
        #print("\npos final:\n ", final)
        #print("\nmapa:\n ", mapa)
        fila = queue.Queue() # Fila para BFS
        #print(mapa,"\n\n", inicial, final)
        grafo = Graph(mapa, mapa.shape) # Grafo modelo matriz de adjacência
        #print(grafo.__dict__)
        preparacaoBFS()
        ##caminho.reverse()
        ##for passo in caminho:
        ##    print(passo, end="")
        #print(grafo.vertices[100].getPosicao())
        #print(mapa.shape)
        #print(grafo.getCusto(inicial))