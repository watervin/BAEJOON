from collections import deque
import sys

d = deque()
n = int(input())

for i in range(n):
    user = sys.stdin.readline().split()

    if user[0] == "push_front":
        d.appendleft(user[1])
    elif user[0] == "push_back":
        d.append(user[1])
    elif user[0] == "pop_front":
        if d:
            print(d[0])    
            d.popleft()
        else:
            print("-1")
    elif user[0] == "pop_back":
        if d:
            print(d[len(d) - 1])    
            d.pop()
        else:
            print("-1")
    elif user[0] == "size":
        print(len(d))
    elif user[0] == "empty":
        if d:
            print("0")
        else:
            print("1")
    elif user[0] == "front":
        if d:
            print(d[0])
        else:
            print("-1")
    elif user[0] == "back":
        if d:
            print(d[len(d) - 1])
        else:
            print("-1")