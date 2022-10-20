N, K = map(int, input().split())

seq = [i+1 for i in range(N)]
real_k = K-1

ans = []
while seq:
  while real_k >= len(seq):
    real_k -= len(seq)
  ans.append(seq.pop(real_k))
  real_k += K-1
print("<", end="")
cnt = 1
for i in ans:
  if cnt < N:
    print(i , end=", ")
    cnt += 1
  else: print(i, end="")
print(">")