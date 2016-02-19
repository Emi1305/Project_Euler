'''A Pythagorean triplet is a set of three natural numbers, a<b<ca<b<c, for which,
    a**2+b**2=c**2
Given NN, Check if there exists any Pythagorean triplet for which a+b+c=Na+b+c=N
Find maximum possible value of abcabc among all such Pythagorean triplets, If there is no such Pythagorean triplet print −1−1.'''

from math import sqrt

for _ in range(int(input())):
    n = int(input())
    posibles = list()
    for a in range(1,n):
        b = (n**2 - 2*a*n)/(2*n - 2*a)
        if b.is_integer():
            b = int(b)
            c = n-a-b
            if b<=0 or c<=0:
                continue
            posibles.append(a*b*c)
    try:
        print(max(posibles))
    except:
        print(-1)
