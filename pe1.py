'''Find the sum of all the multiples of 3 or 5 below N. '''

def sumaDeDivisores(n, divisor):
    '''
    :param n:
    :param divisor:
    :return: Suma todos los numeros menores a n que son divisibles por "divisor"
    '''

    #Formula de la sumatoria de los elemntos de una serie x*(x+1)//2
    return (n//divisor)*(divisor*(1+(n//divisor)))//2

for _ in range(int(input())):
    N = int(input())-1 #Le resto uno porque son los divisores estrictamente menores al numero ingresado
    print(sumaDeDivisores(N,3) + sumaDeDivisores(N, 5) - sumaDeDivisores(N, 15))