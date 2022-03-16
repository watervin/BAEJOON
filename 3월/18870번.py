num = int(input())
lists = list(map(int,input().split()))

lists_sort = sorted(list(set(lists)))

dic = {lists_sort[i]:i for i in range(len(lists_sort))}

for i in lists:
    print(dic[i],end=" ")