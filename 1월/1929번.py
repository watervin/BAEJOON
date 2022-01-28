#1929번 소수구하기

num1, num2 = map(int, input().split())

for number in range(num1, num2+1):
    if number == 1: 
        continue
    for j in range(2, int(number** 0.5)+1 ):
        if number%j==0:
            break
    else:
        print(number)