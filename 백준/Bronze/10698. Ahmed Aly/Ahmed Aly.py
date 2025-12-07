T = int(input())
for i in range(T):
  x,op,y,eq,z = input().split()
  X = int(x)
  Y = int(y)
  Z = int(z)
  
  if op == '+':
    if X+Y == Z:
      print(f"Case {i+1}: YES")
    else:
      print(f"Case {i+1}: NO")
  elif op == '-':
    if X-Y == Z:
      print(f"Case {i+1}: YES")
    else:
      print(f"Case {i+1}: NO")


  