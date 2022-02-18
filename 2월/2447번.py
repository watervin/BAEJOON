def make_stars(n):
    
    Temp = []
    for i in range(3 * len(n)):
        if i // len(n) ==  1:
            Temp.append(n[i % len(n)] + " " * len(n) + n[i % len(n)])
        else:
            Temp.append(n[i % len(n)] * 3)
    
    return Temp



stars = ["***", "* *", "***"]
n = int(input())
k = 0

while n != 3:
    n = int(n / 3)
    k += 1

for i in range(k):
    stars = make_stars(stars)
for i in stars:
    print(i)