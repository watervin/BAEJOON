n,m = map(int,input().split()) #n 숫자범위 m갯수
 
lists = []
 
def dfs():
    if len(lists)==m:
        print(' '.join(map(str,lists)))
        return
    
    for i in range(1,n+1):
            lists.append(i)
            dfs()
            lists.pop()
 
dfs()