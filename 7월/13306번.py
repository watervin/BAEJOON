#13306번

n = int(input())
road = list(map(int,input().split(" ")))
price = list(map(int,input().split(" ")))
small = price[0]

total = 0 
for i in range(n-1):
    if price[i] >= small:
        total += small * road[i]
    elif price[i] < small:
        small = price[i]
        total += small * road[i]
print(total)
