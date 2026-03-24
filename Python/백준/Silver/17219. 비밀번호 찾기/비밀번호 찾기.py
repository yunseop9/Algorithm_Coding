import sys
input = sys.stdin.readline
#저장된 사이트 주소 수n, 비밀번호 찾으려는 사이트 주소 수m
n,m = map(int,input().split())

dict = {}

for _ in range(n):
    addr, pw = input().split()
    dict[addr] = pw
    
for _ in range(m):
    addr = input().strip()
    print(dict[addr])