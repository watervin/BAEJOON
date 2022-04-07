from math import factorial

n,m = list(map(int,input().split()))

result = factorial(n)//(factorial(m)*(factorial(n-m)))
print(result%10007)