#15662번

n,m = map(int,input().split()) #n 숫자범위 m갯수
 
lists = []
 
def dfs(start):
    if len(lists)==m:
        print(' '.join(map(str,lists)))
        return
    
    for i in range(start,n+1):
            lists.append(i)
            dfs(i)
            lists.pop()
 
dfs(1)