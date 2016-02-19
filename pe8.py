'''ind the greatest product of KK consecutive digits in the NN digit number.

Input Format
First line contains T that denotes the number of test cases.
First line of each test case will contain two integers N & K.
Second line of each test case will contain a N digit integer. '''

from functools import reduce

def multiplicacion(numeros):
    '''
    Retorna el resultado de multiplicar los numeros de una lista
    :param numeros:
    :return:
    '''
    return reduce(lambda x, y: x*y, numeros, 1)

for _ in range(int(input())):
    _, cant  = map(int, input().split()) #Descarto la cantidad de digitos que tiene la entrada
    numeros = [int(i) for i in input()]
    maximo = 0
    for i in range(len(numeros)-cant):
        s = multiplicacion(numeros[i:i + cant])
        maximo = maximo if maximo > s else s
    print(maximo)
