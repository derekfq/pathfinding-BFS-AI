from file import *
from grafo import *
import queue
import pandas as pd
import numpy as np
import pygame
np.set_printoptions(threshold=np.inf)
import math
WIDTH = 600
HEIGTH = 600
WIN = pygame.display.set_mode((WIDTH, HEIGTH))
pygame.display.set_caption("Busca em largura ")

RED = (255, 0, 0) #fogo
GREEN = (0, 255, 0) #Sólido e plano
BLUE = (0, 0, 255) #Pantano
BROWM =(165, 42, 42) #Montanhoso
GREY = (128, 128, 128) #PRA DESENHAR OS QUADRADOS
YELLOW = (255, 255, 0) #visitado
PURPLE = (128, 0, 128) #caminho mais curto
ORANGE = (255, 165 ,0) #começo
TURQUOISE = (64, 224, 208) #fim
PINK = (255, 203, 219) #fila


# Posição dentro da matriz do front-end
class Spot:
    def __init__(self, width, height, total_rows,total_cols,pos,arestas,custo):
        self.row = pos[1] #ver como esta sendo tratado para mandar uma lista com x y
        self.col = pos[0]
        self.x = self.row * width
        self.y = self.col * height
        self.color = GREEN
        self.width = width
        self.cols = total_cols
        self.total_rows = total_rows
        self.heigth = height
        self.pos = pos #lista com x e y
        # Atribui as cores para cada posição considerando o custo de cada uma
        if custo == 1:
            self.custo = custo
            self.color = GREEN
        elif custo == 2:
            self.custo = 5
            self.color = BROWM
        elif custo == 3:
            self.custo = 10
            self.color = BLUE
        elif custo == 4:
            self.custo = 15
            self.color = RED
        self.arestas = arestas #lista de vizinhos
        self.posicaoAnterior = None
        self.custoTotal = None

    def setCustoTotal(self, custo):
        self.custoTotal = custo

    def setPosicaoAnterior(self, posicao):
        self.posicaoAnterior = posicao

    def get_pos(self):
        return self.pos

    def is_closed(self): #já passou pelo nó
        return self.color == YELLOW

    def is_open(self): #esta vendo esse/esses nós agora
        return self.color == GREEN

    def is_start(self):
        return self.color == ORANGE

    def is_end(self):
        return self.color == TURQUOISE

    def is_fila(self):
        return self.color == PINK

    def make_fila(self):
        self.color = PINK

    def make_start(self):
        self.color = ORANGE

    def make_closed(self):
        self.color = YELLOW

    def make_open(self):
        self.color = GREEN

    def make_end(self):
        self.color = TURQUOISE

    def make_path(self):
        self.color = PURPLE

    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.heigth))

    def getCusto(self):
        return self.custo

    def getCustoTotal(self):
        return self.custoTotal

    def getPosicaoAnterior(self):
        return self.posicaoAnterior

    # Se a posição não existir
    def __lt__(self, other):
        return False


class Graph(object):
    def __init__(self, matriz, shape):
        self.vertices = [] # define uma lista de vértices
        self.linha = matriz.shape[0] # tamanho da linha
        self.coluna = matriz.shape[1] # tamanho da coluna
        # define as dimensões da tela do mapa
        gapw = 600 //  self.linha
        gaph = 600 //  self.coluna
        for i in range(shape[0]):
            for j in range(shape[1]):
                arestas = [] # define uma lista de posições adjacentes
                if i-1 >= 0:
                    arestas.append([i-1, j]) # Norte
                if j+1 <= range(shape[1])[-1]:
                    arestas.append([i, j+1]) # Leste
                if i+1 <= range(shape[0])[-1]:
                    arestas.append([i+1, j]) # Sul
                if j-1 >= 0:
                    arestas.append([i, j-1]) # Oeste
                self.vertices.append(Vertice([i,j],arestas,matriz[i][j]))

    def getVertices(self):
        return self.vertices

    # retorna a representação do grafo em string
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


#Faz os quadrados
def make_grid(rows,cols, width, height,matriz): #fazer receber a matriz para passar o valor, mandar o valor pro spot e la define a cor
    grid = []
    gapw = width // cols # tamanho das colunas
    gaph = height //  rows # tamanho das linhas
    for i in range(rows):
        grid.append([]) # posições adjacentes
        for j in range(cols):
            arestas = []
            if i-1 >= 0:
                arestas.append([i-1, j]) # Norte
            if j+1 <= range(rows)[-1]:
                arestas.append([i, j+1]) # Leste
            if i+1 <= range(cols)[-1]:
                arestas.append([i+1, j]) # Sul
            if j-1 >= 0:
                arestas.append([i, j-1]) # Oeste
            spot = Spot(gaph , gapw, rows, cols,[i,j],arestas,matriz[i][j])
            grid[i].append(spot) 
    return grid


#desenha o contorno dos quadrados
def draw_grid(win, rows,cols , width):
    gap = width // rows
    gap2 = width // cols
    for i in range(rows):
        pygame.draw.line(win, GREY, (0, i * gap), (width, i * gap))
        for j in range(cols):
            pygame.draw.line(win, GREY, (j * gap2, 0), (j * gap2, width))

# loop para o desenho das posições
def draw(win, grid, rows,cols, width):
    #win.fill(RED)

    for row in grid:
        for spot in row:
            spot.draw(win)
    # desenha as posições na tela
    draw_grid(win, rows,cols, width)
    pygame.display.update()

def BFS(posAtual,ini,fim,grid):
    # verifica se a fila é vazia
    if posAtual == queue.Empty:
        return
    # calcula o custo total na posição
    grafo.setCustoTotal(posAtual, grafo.getCustoTotal(grafo.getPosicaoAnterior(posAtual)) + grafo.getCusto(posAtual))
    # Verifica se chegou no destino
    if posAtual == fim:
        print("Caminho encontrado (destino->início):")
        #print(grafo.__dict__)
        # Exibe o caminho encontrado
        exibeCaminho(posAtual,grid)
        print("\nCusto total:", grafo.getCustoTotal(posAtual))
        return
    # 
    for vertice in grafo.getArestas(posAtual):
        # muda a cor da posição desconsiderando a posição inicial
        if posAtual != ini:
            aux1 = posAtual[0]
            aux2 = posAtual[1]
            grid[aux1][aux2].make_closed() # posição que foi visitada
        if grafo.getPosicaoAnterior(vertice) == None:
            grafo.setPosicaoAnterior(vertice, posAtual)
            aux3 = vertice[0]
            aux4 = vertice[1]
            grid[aux3][aux4].make_fila()
            fila.put(vertice)
    BFS(fila.get(block=False),ini,fim,grid)

def preparacaoBFS(ini,fim,grid):
    fila.put(ini) #Coloca dentro da fila a posição inicial
    grafo.setPosicaoAnterior(ini, 0) # coloca a posição anterior como 0, identificando que é a posição inicial
    BFS(fila.get(),ini,fim,grid) # inicia a busca em largura

def exibeCaminho(posicao,grid):
    if posicao == 0:
        return

    aux1 = posicao[0]
    aux2 = posicao[1]
    grid[aux1][aux2].make_path() # exibe o caminho no front
    ##print(posicao, end="")
    ##caminho.append(posicao)
    # Muda a cor da célula, exibindo o caminho
    # Recursão chamando noAnterior

    exibeCaminho(grafo.getPosicaoAnterior(posicao),grid)

# MAIN
path = OpenFile()
if path != '':
    #print("path: \n", path)
    matriz = pd.read_csv(path, header = None).fillna(-1).to_numpy(dtype=int)
    aux1 = matriz[0][0]
    aux2 = matriz[0][1]
    aux3 = matriz[1][0]
    aux4 = matriz[1][1]
    ini =[aux1,aux2]
    fin = [aux3,aux4]
    mapa = np.delete(matriz,[0,1],0)
    ROWS, COLS = mapa.shape
    grid = make_grid(ROWS, COLS, WIDTH, HEIGTH, mapa)
    start = grid[aux1][aux2]
    end = grid[aux3][aux4]
    # verifica se a matriz contém uma posição final, inicial, e se a matriz não contém uma posição que está faltando
    if CoordTest(ini, ROWS, COLS) == True and CoordTest(fin,ROWS,COLS) == True and MapCheck(mapa) == True and ini != fin:            
        fila = queue.Queue()
        grafo = Graph(mapa, mapa.shape)
        start.make_start()
        end.make_end()
        run = True
        while run:
            draw(WIN, grid, ROWS, COLS, WIDTH)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE and start and end:
                        preparacaoBFS(ini,fin,grid)
        pygame.quit()


