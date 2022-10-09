N = int(input())
A = list(map(int, input().split()))
dp = [0] * N
dp_reverse = [0] * N
bitonic_list = [0] * N
for i in range(N):
  for j in range(i):
    if A[j] < A[i] and dp[i] < dp[j]:
      dp[i] = dp[j]
  dp[i] += 1
for i in range(-1, -N-1, -1):
  for j in range(-1, i, -1):
    if A[j] < A[i] and dp_reverse[i] < dp_reverse[j]:
      dp_reverse[i] = dp_reverse[j]
  dp_reverse[i] += 1
for i in range(N):
  bitonic_list[i] = dp[i] + dp_reverse[i] - 1
print(max(bitonic_list))