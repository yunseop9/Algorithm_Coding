import sys

input = sys.stdin.readline

n = int(input().strip())

result = 0

def digit_sum(x):
    total = 0
    while x > 0:
        total += x %10
        x //= 10
    return total

for i in range(n):
    if i + digit_sum(i) == n:
        result = i
        break
        
print(result)