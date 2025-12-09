N = int(input().strip()) #과목의 개수
nowScore = list(map(int,input().split())) #현재 시험 점수 리스트
M = max(nowScore) #최고 점수

newScore = 0 #사기친 점수 합
for i in range(N):
  newScore += nowScore[i]/M*100

print(newScore/N)