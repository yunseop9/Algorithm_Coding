T = int(input())
for i in range(T):
  x,op,y,eq,z = input().split()
  X,Y,Z = int(x),int(y),int(z)

  
  if op == '+':
    cal = X + Y
  elif op == '-':
    cal = X - Y
  
  if cal == Z:
    print(f"Case {i+1}: YES")
  else:
    print(f"Case {i+1}: NO")

  