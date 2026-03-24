import sys
input = sys.stdin.readline
n = int(input()) #상근이가 가지고 있는 카드 개수

nCard = list(map(int, input().split())) #n개의 카드에 뭐가 적혀있는지

m = int(input()) #정수 m개가 주어짐

#m으로 입력받은 숫자들을 상근이가 몇 개나 가지고 있는지
mCard = list(map(int, input().split())) 

dict = {}

for card in nCard:
    if card in dict:
        dict[card] += 1
    else:
        dict[card] = 1
        
for card in mCard:
     print(dict.get(card, 0), end = " ")