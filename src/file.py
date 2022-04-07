from tkinter import Tk
from tkinter.filedialog import askopenfilename

def OpenFile(): # Abre a interface para selecionar um arquivo CSV
    ftypes = [('Arquivo CSV','*.csv')]
    Tk().withdraw()
    return askopenfilename(filetypes=ftypes)

def CoordTest(Coord, rows, columns): # Verifica coordenada
    if Coord[0] == -1 or Coord[1] == -1:
        print(Coord, " faltam dados\n")
        return False
    if Coord[0] >= rows or Coord[0] < 0 or Coord[1] >= columns or Coord[1] < 0:
        print(Coord, " inválida\n")
        return False
    return True

def MapCheck(map): # Checa se o mapa possui apenas informações do terreno dentro do intervalo esperado
    for num in map.flatten():
        if num <= 0 or num > 4:
            print("Mapa inválido\n")
            return False
    return True
