def fib():
    '''
    :return: Generador de numeros de fibonacci
    '''
    a, b = 0, 1
    while(True):
        if (a+b) % 2 == 0:
            yield a+b
        a, b = b, a+b


def sumarMenores(x):
    '''
    Suma todos los numeros de la serie de fibonacci que sean menores a x
    :param x:
    :return:
    '''
    rst = 0
    for f in fib():
        if f <= x:
            rst += f
        else:
            return rst

for _ in range(int(input())):
    print(sumarMenores(int(input())))