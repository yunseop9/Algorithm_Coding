import sys

n = int(sys.stdin.readline())
target = [int(sys.stdin.readline()) for _ in range(n)]
stack = []
result = []
targetIndex = 0

for i in range(1,n+1):
    stack.append(i)
    result.append("+")
    while stack and stack[-1] == target[targetIndex]:
        stack.pop()
        result.append("-")
        targetIndex += 1

if len(result) == 2 * n:
    print("\n".join(result))
else:
    print("NO")