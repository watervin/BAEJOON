# 한수는 지금 (x, y)에 있다.
# 직사각형은 각 변이 좌표축에 평행하고,
# 왼쪽 아래 꼭짓점은 (0, 0), 오른쪽 위 꼭짓점은 (w, h)에 있다.
# 직사각형의 경계선까지 가는 거리의 최솟값을 구하기
import math

x,y,w,h = map(int,input().split())

num1 = abs(x-w)
num2 = abs(y-h)

min_value = min(x,y,num1,num2)
print(min_value)