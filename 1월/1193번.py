
x =int(input())
line = 1

while x>line: #x가 4
    x -= line #x는 3이됨
    line += 1 #line은 2가 됨

if line %2 == 0: #짝수일경우
        left  = x
        right = (line-x)+1
else : #홀수일경우
        left  = (line-x)+1
        right = x

print(f"{left}/{right}")




