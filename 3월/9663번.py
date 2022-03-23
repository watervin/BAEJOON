#9663번

n = int(input()) #숫자받기

ans = 0
Chess = [0] * n #체스판?

def queen_ok(x): #퀸을 놓을 수 있는지 없는지
    for i in range(x):
        if Chess[x] == Chess[i] or abs(Chess[x] - Chess[i]) == abs(x - i):
            return False
    
    return True

def n_queens(x):
    global ans
    if x == n:
        ans += 1
        return

    else:
        for i in range(n):
            # [x, i]에 퀸을 놓겠다.
            Chess[x] = i
            if queen_ok(x):
                n_queens(x+1)

n_queens(0)
print(ans)