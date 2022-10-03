n = int(input())
amount = [0]
dp = [0] * (n+1)
for i in range(n):
  a = int(input())
  amount.append(a)
dp[1] = amount[1]
if n > 1:
  dp[2] = amount[1] + amount[2]
for i in range(3, n + 1):
  dp[i] = max(amount[i] + dp[i-2], amount[i] + dp[i-3] + amount[i-1], dp[i-1])
print(max(dp))
# dp[i-1]을 뺴먹음