import sys
input=sys.stdin.readline

N = int(input())

for _ in range(N):
  stack = []
  vps = input()
  i = 0
  already = True
  for char in vps:
    if len(stack) == 0 and char ==")":
      print("NO")
      already = False
      break
    elif char == "(":
      stack.append(1)
    elif char == ")":
      stack.pop()
    i += 1
  if len(stack) == 0 and i == len(vps):
    print("YES")
  else:
    if already:
      print("NO")