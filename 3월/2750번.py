n = int(input())
llist = []
for i in range(n):
    num = int(input())
    llist.append(num)
llist.sort()
for i in range(n):
    print(llist[i])
