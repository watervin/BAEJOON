#2562번
arr = []
for i in range(9):
    arr.append(int(input()))
big = max(arr)
print(big)
print(arr.index(big)+1)