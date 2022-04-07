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
        self.posicaoAnterior = None # Posição anterior para denotar o caminho e demarcar se o nó está presente na fila
        self.custoTotal = None # Denota o custo total até o momento no presente nó, denota também se o nó já foi visitado

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



