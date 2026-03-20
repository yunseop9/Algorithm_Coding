import sys

input = sys.stdin.readline

while True:
    sentence = input().rstrip()
    if sentence == ".":
        break
    
    stack =[]
    balance = True

    for char in sentence:
        if char == "(":
            stack.append(char)
        if char == "[":
            stack.append(char)
        if char == ")":
            if stack and stack[-1] == "(":
                stack.pop()
            else:
                balance = False
                break
        if char == "]":
            if stack and stack[-1] =="[":
               stack.pop()
            else:
                balance = False
                break
            
    if not stack and balance == True:
        print("yes")
    else:
        print("no")
            
            