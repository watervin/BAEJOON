n,k = map(int,input().split())
coin = list()
for i in range(n):
    coin.append(int(input()))
coin.sort(reverse=True)
check = 0

for i in range(n):
    check += k // coin[i]
    k = k % coin[i]
print(check)