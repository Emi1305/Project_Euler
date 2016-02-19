'''Find the sum of all the primes not greater than given N.'''


from math import sqrt
from bisect import bisect_left

def masCercano(lista, buscado):
    '''
    Retorna el buscado si se encuentra en la lista o el menor mas cercarno si no estuviese
    :param lista:
    :param buscado:
    :return:
    '''
    pos = bisect_left(lista, buscado)
    #Si el bisect_left devuelve el primer o el ultimo elemento de la lista lo retorno
    if pos == 0:
        return lista[0]
    if pos == len(lista):
        return lista[-1]
    anterior = lista[pos - 1]
    siguiente = lista[pos]
    if siguiente == buscado: #Si el numero buscado es parte de la lista se retorna el numero exacto
        return siguiente
    else: #Sino retorno el primo inmediatamente anterior
        return anterior
primos = [2]
def cribar(n):
    '''
    Emplea el metodo de la criba de Erastostenes para generar todos los numeros primos hasta n
    :param n:
    :return:
    '''
    todos = list(range(3, n+1, 2))
    i = 0
    while(todos[i]**2 <n):
        todos = [x for x in todos if x==todos[i] or x%todos[i] != 0]
        i += 1
    global primos
    primos.extend(todos)

cribar(10**6) #Busco todos los numeros primos hasta 10**6 (

acumulado = 0
sumas = dict()
for p in primos:
    acumulado += p
    sumas[p] = acumulado #Almaceno el resultado de sumar todos los primos menores a p

for _ in range(int(input())):
    n = int(input())
    print(sumas[masCercano(primos, n)]) #Accedo a la suma precalculada del numero primo mas cercano al numero buscado