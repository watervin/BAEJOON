#2675번
roop = int(input())
for n in range(roop):
    nums, arr  = input().split()
    for i in arr:
        print(i * int(nums),end="")
    print("")

