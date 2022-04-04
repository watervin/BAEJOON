n,new,p = map(int,input().split())
lists = []
if n == 0:
    print(1)
else:
    lists = list(map(int,input().split()))
    lists.append(new)
    lists.sort(reverse=True)
    idx = lists.index(new) + 1

    if idx > p:
        print(-1)
    else:
        if p == n and new == lists[-1]:
            print(-1)
        else:
            print(idx)
