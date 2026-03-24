import sys
input = sys.stdin.readline

name_to_num = {}
num_to_name = {}

n, m = map(int,input().split())

for i in range(1, n+1):
    poke = input().strip()
    name_to_num[poke] = i
    num_to_name[i] = poke

for _ in range(m):
    f = input().strip()
    
    if f.isdigit():
        print(num_to_name[int(f)])
    else:
        print(name_to_num[f])
    