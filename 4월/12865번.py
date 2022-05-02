#12865번

#n개 물건 w무게 v가치
#k무게의 배낭
import sys


n,k = map(int,sys.stdin.readline().split())
item = [0] * (k+1)

for i in range(n):
    w,v =  map(int,sys.stdin.readline().split())
    for j in range(k,w-1,-1):
        item[j] = max(item[j],item[j-w]+v)
print(item[-1])
