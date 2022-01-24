num = int(input())
nums = list(map(int,input().split()))
count = 0
for number in nums:
    if number !=1:
        for i in range(2,number):
            if number % i ==0:
                break
        else :
            count += 1

print(count)        