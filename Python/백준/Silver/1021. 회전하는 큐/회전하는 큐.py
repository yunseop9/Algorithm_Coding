import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
target = list(map(int, sys.stdin.readline().split()))
dq = deque(range(1,N+1))
count = 0

for i in range(M):
    if dq.index(target[i]) <= len(dq) // 2:
        while dq[0] != target[i]:
            dq.rotate(-1)
            count += 1
    else:
        while dq[0] != target[i]:
            dq.rotate(1)
            count += 1
    dq.popleft()

print(count)