
N, M = map(int, input().split())
table = [[0] * (N + 1)]
for _ in range(N):
  a = list(map(int , input().split()))
  table.append([0] + a)

# 누적합 구하기
for i in range(N+1):
  for j in range(N+1):
    table[i][j] += table[i-1][j] + table[i][j-1] - table[i-1][j-1]

for _ in range(M):
  x1, y1, x2, y2 = map(int, input().split())
  answer = table[x2][y2] - table[x2][y1-1] - table[x1-1][y2] + table[x1-1][y1-1]
  print(answer)