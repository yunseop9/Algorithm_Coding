N = int(input())

def digit_sum(x):
    sum = 0
    while x > 0:
        sum += x % 10
        x //= 10
    return sum

con = 0
for i in range(N):
    if i + digit_sum(i) == N:
        con = i
        break
     
print(con)