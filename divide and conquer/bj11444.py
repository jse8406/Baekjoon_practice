# 피보나치 수열 규칙 
# n이 짝수인 경우: F(n) = F(n//2+1)^2 - F(n//2-1)^2
# n이 홀수인 경우: F(n) = F(n//2+1)^2 + F(n//2)^2

dp = dict()

n = int(input())

def fibo(n):
  if dp.get(n) != None: # 메모제이션을 안했다. dp에 저장한 데이터 재사용.
    return dp[n]
  if n == 0:
    return 0
  elif n == 1 or n == 2:
    return 1
  else:
    if n % 2 == 0:
      dp[n//2 + 1] = fibo(n//2 + 1) % 1000000007
      dp[n//2 - 1] = fibo(n//2 - 1) % 1000000007
      return dp[n//2 + 1]**2 - dp[n//2 - 1]**2
    else:
      dp[n//2 + 1] = fibo(n//2 + 1) % 1000000007
      dp[n//2] = fibo(n//2) % 1000000007
      return dp[n//2 + 1]**2 + dp[n//2]**2
print(fibo(n) % 1000000007)