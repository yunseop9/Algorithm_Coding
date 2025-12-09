N = int(input().strip()) #과목의 개수
score = list(map(int,input().split())) #현재 시험 점수 리스트
M = max(score) #최고 점수

print(sum(score) / M * 100 / int(N))