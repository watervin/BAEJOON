n, m = map(int, input().split())
alist = []
count = []

for _ in range(n):
    alist.append(input())

for a in range(n-7):
    for b in range(m-7):
        num1 = 0
        num2 = 0
        for i in range(a, a+8):
            for j in range(b, b+8):
                if (i+j) % 2 == 0:
                    if alist[i][j] != 'W':
                        num1 += 1
                    else: 
                        num2 += 1
                else:
                    if alist[i][j] != 'B':
                        num1 += 1
                    else:
                        num2 += 1
        count.append(min(num1, num2))

print(min(count))