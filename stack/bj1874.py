def top(stack:list):
  if stack:
    return stack[-1]

stack = []
answer = []
n = int(input())
seq = []
for i in range(1, n+1):
  s = int(input())
  seq.append(s)
seq.reverse()
for i in range(1, n+1):
  if not stack or top(stack) != seq[-1]:
    stack.append(i)
    answer.append("+")
  while len(seq) > 0 and top(stack) == seq[-1]:
    stack.pop()
    seq.pop()
    answer.append("-")
if stack:
  print("NO")
else:
  print(*answer, sep='\n')