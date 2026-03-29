from collections import deque

n = int(input())
dq = deque(range(1,n+1))
result = []

while len(dq) > 1:
    result.append(dq.popleft())
    dq.rotate(-1)



result.append(dq[0])

print(*result)
