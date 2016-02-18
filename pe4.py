'''A palindromic number reads the same both ways. The smallest 6 digit palindrome made from the product of two 3-digit numbers is 101101=143×707101101=143×707.

Find the largest palindrome made from the product of two 3-digit numbers which is less than NN.'''

def palindrome(string):
    ''' Indica si el string ingresado es un palindromo
    :param string:
    :return:
    '''
    return list(string) == list(reversed(string))

numeros = {i*j for i in range(100, 1000) for j in range(100, 1000) if palindrome(str(i*j))}

for _ in range(int(input())):
    n = int(input())
    print(max(filter(lambda x: x<n, numeros)))