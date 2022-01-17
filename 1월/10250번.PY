# W : 방의 갯수 
# H : 층수
# 방 번호는 YXX나 YYXX형태 Y는 층 XX는 엘베기준

t = int(input())
for i in range(t):
    h, w, n = map(int, input().split())
    xx= n//h+1
    yy= n % h
    if n%h == 0:
        xx=n//h
        yy = h  
        
    print(f'{yy*100+xx}')





