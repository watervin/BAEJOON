import sys

input = sys.stdin.readline

N,M =map(int,input().split())
arr_list = list(map(int,input().split()))

list_sum = [0]
total = 0
for i in range(len(arr_list)):
    total += arr_list[i]
    list_sum.append(total)

for i in range(M):
    i, j = map(int,input().split())
    print(list_sum[j]-list_sum[i-1])

