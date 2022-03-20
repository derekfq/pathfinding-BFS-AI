from buscacega import Graph
import queue

"""
inicializa grafo
seta posição inicial na fila (coloca os valores certos nos atributos na posição inicial do grafo)
BFS(dequeue(), NONE)
"""
def preparacaoBFS():
    grafo = Graph(mat, mat.shape)
    fila.put(inicial) # @FRONT -> mudar a cor para posição inicial
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
    grafo[posAtual[0]][posAtual[1]].setCustoTotal(
        grafo[posAtual[0]][posAtual[1]]
            .getNoAnterior()
            .getCustoTotal()
        +
        grafo[posAtual[0]][posAtual[1]]
            .getcusto()
    )
    if posAtual == destino:
        exibeCaminho(grafo[posAtual[0]][posAtual[1]]) # Ou anterior?? Critério do FRONT
        print(grafo[posAtual[0]][posAtual[1]].getCustoTotal())
        return
    for vertice in grafo[posAtual[0]][posAtual[1]].getVertices():
        if grafo[vertice[0]][vertice[1]].getNoAnterior() == None:
            grafo[vertice[0]][vertice[1]].setNoAnterior(grafo[posAtual[0]][posAtual[1]])
            fila.put(vertice)
    BFS(fila.get())
    #return

# @FRONT
# Função que exibe o caminho encontrado
def exibeCaminho(no):
    if no == None:
        return
    print("caminho:")
    # Muda a cor da célula, exibindo o caminho
    # Recursão chamando noAnterior
    exibeCaminho(no.getNoAnterior())

inicial = [] # Posição inicial da busca
destino = [] # Posição destino
fila = queue.Queue() # Fila para BFS
mat = []
grafo = [] # Grafo modelo matriz de adjacência