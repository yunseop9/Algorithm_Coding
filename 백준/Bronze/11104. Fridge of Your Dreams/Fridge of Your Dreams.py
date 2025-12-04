n = int(input().strip())
for _ in range(n):
    b = input().strip()
    dec = 0
    
    for ch in b:
        dec = dec * 2
        if ch == '1':
            dec += 1
    print(dec)