import sys
n = int(sys.stdin.readline())
time = []
for i in range(n):
    start , end = map(int,input().split())
    time.append([start,end])
time.sort(key = lambda x : (x[1],x[0]))

check = 1
end = time[0][1]

for i in range(1,n):
    if time[i][0] >= end:
        check += 1
        end = time[i][1]
print(check)
