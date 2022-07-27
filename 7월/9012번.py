#9012번 파이썬
import sys
n = int(sys.stdin.readline())
for _ in range(n):
    string = list(sys.stdin.readline().strip())
    stack = []
    for i in range(len(string)):
        if string[i] == '(':
            stack.append(string[i])
        elif string[i] == ')':
            if stack:
                stack.pop()
            else:
                print("NO")
                break
    else:
        if not stack:
            print("YES")
        else:
            print("NO")


