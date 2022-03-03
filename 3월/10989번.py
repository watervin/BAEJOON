#10989번 파이썬
import sys

n = int(sys.stdin.readline())
llist = [0] * 10001
for i in range(n):
    llist[int(sys.stdin.readline())]+= 1
    

for i in range(10001):
    if llist[i] !=0:
        for j in range(llist[i]):
            print(i)
