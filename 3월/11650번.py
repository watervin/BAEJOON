#11650번

n = int(input())
lists = []
for i in range(n):
    num1,num2 = map(int,input().split())
    lists.append([num1,num2])


new_lists = sorted(lists)

for i in range(n):
    print(new_lists[i][0],new_lists[i][1])
