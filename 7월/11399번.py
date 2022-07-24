#11399번 파이썬
import sys

n = int(sys.stdin.readline())
people = list(map(int,sys.stdin.readline().split()))


people.sort()
total = 0
for i in range(n):
    total += sum(people[0:i+1])
print(total)
