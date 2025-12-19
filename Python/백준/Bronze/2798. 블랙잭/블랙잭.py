
N,M = map(int,input().split())

cards = list(map(int,input().split()))

best = 0
for i in range(N):
  for j in range(i+1,N):
    for k in range(j+1,N):
      num = cards[i] + cards[j] + cards[k]
      if num <= M and num > best:
        best = num

print(best)