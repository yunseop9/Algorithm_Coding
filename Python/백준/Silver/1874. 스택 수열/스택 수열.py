import sys

input = sys.stdin.readline
n = int(input())

stack = []
result = []
target = [int(input()) for _ in range(n)]
target_idx = 0

for i in range(1,n+1):
    stack.append(i)
    result.append("+")
    
    while stack and stack[-1] == target[target_idx]:
        result.append("-")
        stack.pop()
        target_idx += 1

if not stack:
    print("\n".join(result))
else:
    print("NO")