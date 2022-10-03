N = int(input())
dp = [[0 for _ in range(10)] for _ in range(N)]
for i in range(1,10):
  dp[0][i] = 1
for i in range(1, N):
  dp[i][0] = dp[i][0] + dp[i-1][1]
  dp[i][9] = dp[i][9] + dp[i-1][8]
  for j in range(1,9):
    dp[i][j] = dp[i][j] + dp[i-1][j-1] + dp[i-1][j+1]
print(sum(dp[N-1])%1000000000)

# 0 또는 9로 끝나는 계단 수에 대해 길이가 1 더 긴 계단 수를 만드는 경우의 수는 1개
# 나머지는 2개로 계산