import sys
from collections import deque

input = sys.stdin.readline
N = int(input())
dq = deque()

for _ in range(N):
    myList = input().split()
    cmd = myList[0]

    if cmd == "push_front":
        dq.appendleft(myList[1])
    elif cmd == "push_back":
        dq.append(myList[1])
    elif cmd == "pop_front":
        if not dq:
            print("-1")
        else:
            print(dq.popleft())
    elif cmd == "pop_back":
        if not dq:
            print("-1")
        else:
            print(dq.pop())
    elif cmd == "size":
        print(len(dq))
    elif cmd == "empty":
        if not dq:
            print("1")
        else:
            print("0")
    elif cmd == "front":
        if not dq:
            print("-1")
        else:
            print(dq[0])
    elif cmd == "back":
        if not dq:
            print("-1")
        else:
            print(dq[-1])