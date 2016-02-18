'''Find the difference between the sum of the squares of the first NN natural numbers
and the square of the sum.'''



for _ in range(int(input())):
    n = int(input())

    print((n*(n+1)//2)**2 # formula de la suma de una progesion aritmetica: '(n+1)*(a0 + an)/2'
            -
          (n*(n+1)*(2*n+1)//6)) # Formula de la sumatoria de 2**i de 0 a n