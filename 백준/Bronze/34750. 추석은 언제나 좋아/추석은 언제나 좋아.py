N = int(input().strip())
parents = 0
mine = 0
if N >= 1000000:
  parents += N * 0.2
  mine = N - parents
elif 500000 <= N < 1000000:
  parents += N * 0.15
  mine = N - parents
elif 100000 <= N < 500000:
  parents += N * 0.1
  mine = N - parents
else:
  parents += N * 0.05
  mine = N - parents
print(int(parents), int(mine))
