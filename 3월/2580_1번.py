#두번째 공부

sudoku = [list(map(int,input().split())) for _ in range(9)]
# 줄단위로 받음
# print(sudoku)
zero = [(i,j)for i in range(9) for j in range(9) if sudoku[i][j]==0]

def is_promising(i, j):
    numbers = [1,2,3,4,5,6,7,8,9]

    for k in range(9):
        if sudoku[i][k] in numbers:
            numbers.remove(sudoku[i][k])
        if sudoku[k][j] in numbers:
            numbers.remove(sudoku[k][j])
    
    i //=3
    j //=3
    for p in range(i*3,(i+1)*3):
        for q in range(j*3,(j+1)*3):
            if sudoku[p][q] in numbers:
                numbers.remove(sudoku[p][q])
    return numbers

flag = False 
def dfs(x):
    global flag
    
    if flag: 
        return
        
    if x == len(zero): 
        for row in sudoku:
            print(*row)
        flag = True #답 출력
        return
        
    else:    
        (i, j) = zero[x]
        promising = is_promising(i, j) 
        
        for num in promising:
            sudoku[i][j] = num 
            dfs(x + 1)
            sudoku[i][j] = 0 
dfs(0)
