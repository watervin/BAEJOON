n = int(input())
lists = []
for i in range(n):
    string = str(input())
    lists.append(string)

lists = set(lists)
lists = list(lists)
lists.sort()
lists.sort(key =len)

for i in lists:
    print(i)
