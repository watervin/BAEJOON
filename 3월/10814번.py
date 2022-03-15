#10814번 
n = int(input())
lists = []
for i in range(n):
    age,name = map(str,input().split())
    lists.append([int(age),name])

lists.sort(key=lambda x:x[0])

for i in lists:
    print(*i,sep=" ")