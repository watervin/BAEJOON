h, m, s = map(int,input().split())
num = int(input())


s += num % 60
num = num // 60
if s >= 60:
    s -= 60
    m += 1

m += num % 60
num = num // 60
if m >= 60:
    m -= 60
    h += 1

h += num % 24
if h >= 24:
    h -= 24

print(h,m,s)