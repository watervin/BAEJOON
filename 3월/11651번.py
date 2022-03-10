#11651번

n = int(input())
lists = []
for i in range(n):
    num1,num2 = map(int,input().split())
    change = [num2,num1]
    lists.append(change)


new_lists = sorted(lists)

for i in range(n):
    print(new_lists[i][1],new_lists[i][0])
