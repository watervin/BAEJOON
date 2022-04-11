sum = 0
for n in list(map(int, input().split())):
    sum += n**2
print(sum % 10)
