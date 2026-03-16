T = int(input())

for _ in range(T):
    s = input()
    stack = []
    
    for ch in s:
        if ch == "(":
            stack.append(ch)
        elif stack:
            stack.pop()
        else:
            stack.append(ch)
            break
                
    print("YES" if not stack else "NO")