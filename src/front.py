
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
	def __init__(self, row, col, width, height, total_rows,total_cols):
		self.row = row
		self.col = col
		self.x = row * width
		self.y = col * height
		self.color = BLUE #COR INICIAL DE TUDO
		self.neighbors = []
		self.width = width
		self.cols = total_cols
		self.total_rows = total_rows
		self.heigth = height        

	def get_pos(self):
		return self.row, self.col

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


	def __lt__(self, other):
		return False

#Faz os quadrados
def make_grid(rows,cols, width, height): #fazer receber a matriz para passar o valor, mandar o valor pro spot e la define a cor
	grid = []
	gapw = width // rows
	gaph = height //  cols    
	for i in range(rows):
		grid.append([])
		for j in range(cols):
			spot = Spot(i, j, gaph , gapw, rows, cols)
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
	win.fill(RED)

	for row in grid:
		for spot in row:
			spot.draw(win)

	draw_grid(win, rows,cols, width)
	pygame.display.update()

def main(win, width,height):
	ROWS = 40 
	COLS = 40
	grid = make_grid(ROWS, COLS, width, height)
	start = grid[0][0] #colocar o que jao pegou
	start.make_start()
	end = grid[0][1] #colocar o que jao pegou
	end.make_end()
	run = True
	while run:
		draw(win, grid, ROWS, COLS, width)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False

			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_SPACE and start and end:
					for row in grid:
						for spot in row:
							spot.update_neighbors(grid) #equivalente a classe Graph criada no grafo.py
                            #o update neighbors vai andar nos nós vizinhos

					#pode ser usado como main para puxar o algoritmo

				if event.key == pygame.K_c:
					start = None
					end = None
					grid = make_grid(ROWS, COLS, width, height)

	pygame.quit()

main(WIN, WIDTH, HEIGTH)