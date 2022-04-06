from file import *
from grafo import *
import pandas as pd
import numpy as np
import pygame
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
        return self.color == RED

    def is_open(self): #esta vendo esse/esses nós agora
        return self.color == GREEN

    def is_start(self):
        return self.color == ORANGE

    def is_end(self):
        return self.color == TURQUOISE

    def make_start(self):
        self.color = ORANGE

    def make_closed(self):
        self.color = RED

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


    def __lt__(self, other):
        return False

#Faz os quadrados
def make_grid(rows,cols, width, height,matriz): #fazer receber a matriz para passar o valor, mandar o valor pro spot e la define a cor
    grid = []
    gapw = width // cols
    gaph = height //  rows    
    for i in range(rows):
        grid.append([])
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

def draw(win, grid, rows,cols, width):
    #win.fill(RED)

    for row in grid:
        for spot in row:
            spot.draw(win)

    draw_grid(win, rows,cols, width)
    pygame.display.update()

def main(win, width,height):

    path = OpenFile()
    if path != '':
        #print("path: \n", path)
        matriz = pd.read_csv(path, header = None).fillna(-1).to_numpy(dtype=int)
        aux1 = matriz[0][0]
        aux2 = matriz[0][1]
        aux3 = matriz[1][0]
        aux4 = matriz[1][1]
        mapa = np.delete(matriz,[0,1],0)
        ROWS, COLS = mapa.shape
        grid = make_grid(ROWS, COLS, width, height, mapa)
        start = grid[aux1][aux2]
        end = grid[aux3][aux4]




    #start = grid[0][0] #colocar o que jao pegou
    start.make_start()
    #end = grid[0][1] #colocar o que jao pegou
    end.make_end()
    run = True
    while run:
        draw(win, grid, ROWS, COLS, width)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and start and end:
                    algoritmo

                if event.key == pygame.K_c:
                    start = None
                    end = None
                    grid = make_grid(ROWS, COLS, width, height,matriz)

    pygame.quit()

main(WIN, WIDTH, HEIGTH)