n = int(input().strip())
nums = map(int,input().split())
total = sum(nums)
if total > 0:
  print("Right")
elif total == 0:
  print("Stay")
else:
  print("Left")