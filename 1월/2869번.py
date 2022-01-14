#2869번

#높이 v 올라갑니다 a 내려갑니다 b

import math

a,b,v = map(int,input().split())
# 2 1 5
cnt =0 #일
height = 0 #올라간높이

cnt = (v-a)/(a-b)+1
print(math.ceil(cnt))
