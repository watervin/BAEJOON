#14425번
import sys
input = sys.stdin.readline

n , m = map(int,input().split())
arr = set([input() for _ in range(n)])

count = 0

for i in range(m):
    s = input()
    if s in arr :
        count += 1
print(count)