from collections import deque
import sys

n ,k = map(int, sys.stdin.readline().split())
q = deque(range(1,n+1))
l = []

for _ in range(n):
    q.rotate(-(k-1))
    l.append(str(q.popleft()))

print("<" + ", ".join(l) + ">")