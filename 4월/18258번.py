#18258번
import sys
from collections import deque

n = int(sys.stdin.readline())
queue = deque([])

for i in range(n):
    user = sys.stdin.readline().split()

    if user[0] == "push":
        queue.append(user[1])
    elif user[0] == "pop":
        if not queue:
            print(-1)
        else:
            print(queue.popleft())
    elif user[0] == "size":
        print(len(queue))
    elif user[0] == "empty":
        if len(queue) == 0:
            print(1)
        else:
            print(0)
    elif user[0] == "front":
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])
    elif user[0] == "back":
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[-1])       



