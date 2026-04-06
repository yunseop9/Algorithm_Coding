import sys

input = sys.stdin.readline

n, m = map(int, input().split())
board = [input().strip() for _ in range(n)]

def count(x,y):
    white_start = 0
    black_start = 0

    for i in range(8):
        for j in range(8):
            now = board[x+i][y+j]

            # (i+j)가 짝수면 시작색과 같은 색이어야 함
            if (i+j) % 2 == 0:
                if now == "B":
                    white_start += 1
                if now == "W":
                    black_start += 1
            else:
                if now == "W":
                    white_start += 1
                if now == "B":
                    black_start += 1
    return min(white_start, black_start)
    
answer = 64

for i in range(n-7):
    for j in range(m-7):
        answer = min(answer, count(i,j))
        
print(answer)