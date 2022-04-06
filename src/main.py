
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
def preparacaoBFS(ini,fim,grid):
    fila = queue.Queue()
    fila.put(ini) # @FRONT -> mudar a cor para posição inicial
    grafo.setPosicaoAnterior(ini, 0)
    BFS(fila.get(),ini,fim,grid)

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
def BFS(posAtual,ini,fim,grid):
    if posAtual == queue.Empty:
        return
    grafo.setCustoTotal(posAtual, grafo.getCustoTotal(grafo.getPosicaoAnterior(posAtual)) + grafo.getCusto(posAtual))
    if posAtual == fim:
        print("Caminho encontrado (destino->início):")
        #print(grafo.__dict__)
        exibeCaminho(posAtual,grid)
        print("\nCusto total:", grafo.getCustoTotal(posAtual))
        return
    for vertice in grafo.getArestas(posAtual):
        if posAtual != ini:
            aux1 = posAtual[0]
            aux2 = posAtual[1]
            grid[aux1][aux2].make_closed()
        if grafo.getPosicaoAnterior(vertice) == None:
            grafo.setPosicaoAnterior(vertice, posAtual)
            fila.put(vertice)
    BFS(fila.get(block=False),ini,fim,grid)
    #return

# @FRONT
# Função que exibe o caminho encontrado
def exibeCaminho(posicao,grid):
    if posicao == 0:
        return

    aux1 = posAtual[0]
    aux2 = posAtual[1]
    grid[aux1][aux2].make_path()
    ##print(posicao, end="")
    ##caminho.append(posicao)
    # Muda a cor da célula, exibindo o caminho
    # Recursão chamando noAnterior

    exibeCaminho(grafo.getPosicaoAnterior(posicao),grid)

# MAIN
