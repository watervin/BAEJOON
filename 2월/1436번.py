#1436번 영화감독 숌

n = int(input())
number = 666
cnt = 0

while 1:
    if '666' in str(number):
        cnt += 1
    if cnt == n:
        print(number)
        break
    number +=1
