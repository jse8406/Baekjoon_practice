N = int(input())
model = set(map(int, input().split()))
M = int(input())
my = list(map(int, input().split()))

for i in range(M):
  if my[i] in model:
    print(1)
  else:
    print(0)