#2981번 파이썬
from math import gcd
from math import sqrt
import sys

read = sys.stdin.readline
nums = []
interval = []
result = []

n = int(read())

for i in range(n):
    num = int(read())
    nums.append(num)
nums.sort()


for i in range(1,n):
    interval.append(nums[i]-nums[i-1])
prev = interval[0]

for i in range(1, len(interval)):
    prev = gcd(prev,interval[i])

for i in range(2,int(sqrt(prev))+1):
    if prev % i == 0:
        result.append(i)
        result.append(prev//i)
result.append(prev)
result = list(set(result))
result.sort()
print(*result)