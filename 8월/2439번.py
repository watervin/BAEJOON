#2439번
n=int(input())
sum=0
for i in range(n):
    sum+=1
    print(" "*(n-sum)+"*"*sum)