#1427번 파이썬

n = int(input())
lists = []
for i in str(n):
    lists.append(int(i))

lists.sort(reverse = True)

for i in lists:
    print(i,end="")
