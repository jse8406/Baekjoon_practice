test_case = int(input())
dp = [0] * 101
dp[1],dp[2],dp[3],dp[4],dp[5] = 1,1,1,2,2
for i in range(test_case):
  N = int(input())
  for j in range(5, N+1):
    dp[j] = dp[j-1] + dp[j-5]
  print(dp[N])