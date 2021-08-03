#1110번
num = int(input()) #받는 숫자
n = num 
count = 0 #카운트
while 1:
    temp = num//10 + num%10
    new_num = (num % 10) * 10 + temp % 10
    count += 1
    num = new_num
    if new_num == n:
        break
print(count)