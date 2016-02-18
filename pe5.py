'''What is the smallest positive number that is evenly divisible(divisible with no remainder)
by all of the numbers from 1 to N?'''


from collections import Counter
from math import sqrt
from functools import reduce

def isPrime(n):
    '''
    Indica si el numero n es primo
    :param n:
    :return:
    '''
    return all([n%i != 0 for i in range(2, int(sqrt(n))+1)])

def factorizacion(num):
    '''
    Devuelve un Counter con los factores primos del numero num y la cantidad de cada uno
    :param num:
    :return: Counter
    '''
    factores, flag = [], True
    while(flag):
        flag = False
        for i in range(2, num+1):
            if num%i == 0 and isPrime(i):
                num = num//i
                flag = True
                factores.append(i)
    return Counter(factores)

def obtenerPrimos(n):
    '''
    Devuelve un Counter con todos los factores primos de los numeros menores a n
    la cantidad de cada factor primo es la mayor de todas
    :param n:
    :return: Counter
    '''
    primos = Counter()
    for i in range(n+1):
        for (factor, cantidad) in factorizacion(i).items():
            primos[factor] = cantidad if primos[factor] < cantidad else primos[factor]
    return primos

for _ in range(int(input())):

    primos = obtenerPrimos(int(input())) #Obtengo los factores primos que forman el numero buscado
    #print(primos)
    print(reduce(lambda x, y: x*y, primos.elements(), 1)) # Multiplico todos los factores