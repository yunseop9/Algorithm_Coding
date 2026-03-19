import sys

while True:
    sentence = sys.stdin.readline().rstrip()
    if sentence == ".":
        break

    stack = []
    balance = True

    for char in sentence:
        if char == "(":
            stack.append("(")
        elif char == ")":
            if stack and stack[-1] == "(": 
                stack.pop()
            else:
                balance = False
                break
        elif char == "[":
            stack.append("[")
        elif char == "]":
            if stack and stack[-1] == "[":
                stack.pop()
            else:
                balance = False
                break

    if balance == True and not stack:
      print("yes")
    else:
       print ("no")