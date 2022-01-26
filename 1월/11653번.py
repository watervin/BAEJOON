#n이 주어지면 소인수분해 하기

n = int(input()) #6
num =2
while n!=1:
    if n % num == 0:
        n//=num
        print(num)
    else :
        num +=1