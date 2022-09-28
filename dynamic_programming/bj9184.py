dp = [[[0]*21 for _ in range(21)] for _ in range(21)]
def w(a,b,c):
  if a <= 0 or b <= 0 or c <= 0:
    return 1
  elif a>20 or b>20 or c>20:
    return w(20, 20, 20)
  elif dp[a][b][c]: # 만약 필요한 호출 된 값이 있으면 계산하지 않고 저장된 배열에서
    return dp[a][b][c] # 값을 가져와 그대로 사용
  elif a < b and b < c :
    dp[a][b][c] = w(a,b,c-1) + w(a,b-1,c-1) - w(a,b-1,c) 
    return dp[a][b][c]
  else:
    dp[a][b][c] = w(a-1, b,c) + w(a-1,b-1,c) + w(a-1,b,c-1) - w(a-1,b-1,c-1)
    return dp[a][b][c]

ans = []
while True:
  a,b,c = map(int, input().split())
  if a == -1 and b == -1 and c == -1:
    break
  print("w(%d, %d, %d) = %d" %(a,b,c,w(a,b,c)))