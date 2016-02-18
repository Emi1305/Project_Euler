'''By listing the first six prime numbers: 2,3,5,7,112,3,5,7,11 and 1313, we can see that the 6th6th prime is 1313.
What is the NN'th prime number?'''

from math import sqrt

primos = [2, 3]

def isPrime(x):
    '''
    Indica si el numero x es primo comprobando que no sea divisible por los numeros primos ya calculados
    :param x:
    :return:
    '''
    for p in primos:
        if int(sqrt(x)+1)<p:
            return True
        elif x%p == 0:
            return False
    return True


def siguientePrimo():
    '''
    Retorna un generador de numeros primos
    :return:
    '''
    i = 5
    while True:
        if isPrime(i):
            yield i
        i += 2 #Solo se verifica para los impares

p = siguientePrimo()
for _ in range(int(input())):
    n = int(input())
    while(len(primos)<n):
        primos.append(next(p))
    print(primos[n-1])
