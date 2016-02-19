'''What is the greatest product of four adjacent numbers in the same
direction (up, down, left, right, or diagonally) in the 20×20 grid?'''

from functools import reduce
matriz = []

def multiplicar(arr):
    '''
    Multiplica los elementos de una lista
    :param arr:
    :return:
    '''
    return reduce(lambda x, y: x* y, arr, 1)

def maxFilas():
    '''
    Devuelve el valor maximo de multiplicar 4 elementos consecutivos de cualquier fila
    :return:
    '''
    resultado = 0
    for fila in range(len(matriz)):
        for columna in range(len(matriz[fila])-3):
            #print(fila,columna)
            resultado = max([multiplicar(matriz[fila][columna:columna+4]), resultado])
    return resultado

def maxColumnas():
    '''
    Devuelve el valor maximo de multiplicar 4 elementos consecutivos de cualquier columna
    :return:
    '''
    resultado = 0
    for fila in range(len(matriz)-3):
        for columna in range(len(matriz[fila])):
            #print(i,j)
            resultado = max([multiplicar([matriz[fila+n][columna] for n in range(4)]), resultado])
    return resultado

def maxDiagonal():
    '''
    Devuelve el valor maximo de multiplicar 4 elementos consecutivos de cualquier diagonal
    :return:
    '''
    resultado = 0
    #Diagonal principal
    for fila in range(len(matriz)-3):
        for columna in range(len(matriz[fila])-3):
            #print(i,j)
            resultado = max([multiplicar([matriz[fila+n][columna+n] for n in range(4)]), resultado])
    #Diagonal secundaria
    for fila in range(len(matriz)-3):
        for columna in range(3, len(matriz[fila])):
            #print(i,j)
            resultado = max([multiplicar([matriz[fila+n][columna-n] for n in range(4)]), resultado])
    return resultado


for _ in range(20):
    matriz.append(list(map(int, input().split())))

print(max((maxFilas(),maxColumnas(), maxDiagonal())))