import math

N, K = map(int,input().split()) #학생 수, 방 최대 인원 수

W1= W2= W3= W4= W5= W6= M1= M2= M3= M4= M5= M6 = 0

for _ in range(N):
  S, Y = map(int,input().split()) #성별(여자0, 남자1), 학년(1~6)
  if S == 0 and Y == 1:
    W1 += 1
  if S == 0 and Y == 2:
    W2 += 1
  if S == 0 and Y == 3:
    W3 += 1
  if S == 0 and Y == 4:
    W4 += 1
  if S == 0 and Y == 5:
    W5 += 1
  if S == 0 and Y == 6:
    W6 += 1
  if S == 1 and Y == 1:
    M1 += 1
  if S == 1 and Y == 2:
    M2 += 1
  if S == 1 and Y == 3:
    M3 += 1
  if S == 1 and Y == 4:
    M4 += 1
  if S == 1 and Y == 5:
    M5 += 1
  if S == 1 and Y == 6:
    M6 += 1

if W1%K != 0:
  W1 = W1//K + 1
else:
  W1 /= K
if W2%K != 0:
  W2 = W2//K + 1
else:
  W2 /= K
if W3%K != 0:
  W3 = W3//K + 1
else:
  W3 /= K
if W4%K != 0:
  W4 = W4//K + 1
else:
  W4 /= K
if W5%K != 0:
  W5 = W5//K + 1
else:
  W5 /= K
if W6%K != 0:
  W6 = W6//K + 1
else:
  W6 /= K
if M1%K != 0:
  M1 = M1//K + 1
else:
  M1 /= K
if M2%K != 0:
  M2 = M2//K + 1
else:
  M2 /= K
if M3%K != 0:
  M3 = M3//K + 1
else:
  M3 /= K
if M4%K != 0:
  M4 = M4//K + 1
else:
  M4 /= K
if M5%K != 0:
  M5 = M5//K + 1
else:
  M5 /= K
if M6%K != 0:
  M6 = M6//K + 1
else:
  M6 /= K


print(int(W1 + W2 + W3 + W4 + W5 + W6 + M1 + M2 + M3 + M4 + M5 + M6))