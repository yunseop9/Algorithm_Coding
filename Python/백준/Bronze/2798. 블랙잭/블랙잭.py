import sys

input = sys.stdin.readline

n, m = map(int, input().split())

integer = list(map(int, input().split()))

result = 0

for i in range(n): 
    for j in range(i+1,n):
        for k in range(j+1,n):
            total = integer[i]+integer[j]+integer[k]
            
            if total <= m and total > result:
                result = total
                
print(result)