#2525번

hour,min = map(int,input().split())
time = int(input())



hour = (hour +((min+time)//60)) % 24
min = (min+time)%60
print(hour,min)
