import pandas as pd
import numpy as np
np.set_printoptions(threshold=np.inf)
from tkinter import Tk
from tkinter.filedialog import askopenfilename

def OpenFile ():
    ftypes = [('Arquivo CSV','*.csv')]
    Tk().withdraw()
    return askopenfilename(filetypes=ftypes)

def CoordTest(Coord, rows, columns):
    if Coord[0] == -1 or Coord[1] == -1:
        print(Coord, " falta informacao\n")
        return False
    if Coord[0] >= rows or Coord[0] < 0 or Coord[1] >= columns or Coord[1] < 0:
        print(Coord, " invalida\n")
        return False
    return True
def MapCheck(map):
    for num in map.flatten():
        if num <= 0 or num > 4:
            print("mapa invalido\n")
            return False
    return True

while True:
    path = OpenFile()
    if path == '':
        break
    print("path: \n", path)
    matriz = pd.read_csv(path, header = None).fillna(-1).to_numpy(dtype=int)
    inicial = [matriz[0][0], matriz[0][1]]
    final = [matriz[1][0], matriz[1][1]]
    mapa = np.delete(matriz,[0,1],0)
    rows, columns = mapa.shape
    if CoordTest(inicial, rows, columns) == True and CoordTest(final,rows,columns) == True and MapCheck(mapa) == True:
        print("\npos inicial:\n ", inicial)
        print("\npos final:\n ", final)
        print("\nmapa:\n ", mapa)
        break
