import sys

input = sys.stdin.readline

left = list(input().strip())
right = []

m = int(input().strip())

for _ in range(m):
    cmd = input().split()
    if cmd[0] == "L":
        if left:
            right.append(left.pop())
    if cmd[0] == "D":
        if right:
            left.append(right.pop())
    if cmd[0] == "B":
        if left:
            left.pop()
    if cmd[0] == "P":
        left.append(cmd[1])    
        
right.reverse()
print(''.join(left+right))