import sys
input = sys.stdin.readline

s = set()
result = []

n,m = map(int,input().strip().split())

for _ in range(n):
    s.add(input().strip())

for _ in range(m):
    x = input().strip()
    if x in s:
        result.append(x)

result.sort()
       
print(len(result))
print(*result, sep = "\n")