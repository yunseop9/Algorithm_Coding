
N = int(input().strip())
arr = [int(input().strip()) for _ in range(N)]

arr.sort() 
print("\n".join(map(str, arr)))
