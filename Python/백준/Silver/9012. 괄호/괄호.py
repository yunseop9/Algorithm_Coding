T = int(input())

for _ in range(T):
    s = input()
    stack = []
    
    for ch in s:
        if ch == "(":
            stack.append(ch)
        else:
            if stack:
                stack.pop()
            else:
                stack.append(ch)
                break
                
    if stack:
        print("NO")
    else:
        print("YES")