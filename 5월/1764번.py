n , m = map(int,input().split())

a = set()

for i in range(n):
    a.add(input())

b = set()
for i in range(m):
    b.add(input())

ab = sorted(list(a&b))

print(len(ab))
for i in range(len(ab)):
    print(ab[i])