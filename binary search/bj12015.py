from bisect import bisect_left

N = int(input())
seq = list(map(int, input().split()))

stack = []

for i in range(N):
  if not stack or stack[-1] < seq[i]:
    stack.append(seq[i])
  else:
    idx = bisect_left(stack, seq[i])
    stack[idx] = seq[i]
print(len(stack))