'''What is the largest prime factor of a given number N?'''
from math import sqrt

def isPrime(n):
    '''
    Indica si el numero ingresado es primo
    :param n:
    :return:
    '''
    return all([n%i != 0 for i in range(2, int(sqrt(n))+1)])


def largestPrime(num):
    '''
    Encuentra el numero primo mas grande que sea inferior a num
    :param num:
    :return:
    '''
    largest, flag = 0, True
    while(flag):
        flag = False
        for i in range(2, int(sqrt(num))+1):
            if num%i == 0 and isPrime(i):
                num = num//i
                flag = True
                break
    return num



for _ in range(int(input())):
    print(largestPrime(int(input())))