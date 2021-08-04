#1546번
num = int(input())
arr = list(map(int, input().split()))
max_num = max(arr)
avg=0
for i in range(num) :
    arr[i]=arr[i]/max_num *100
    avg += arr[i]
print(round(avg/num, 2))