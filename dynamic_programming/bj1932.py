n = int(input())
tri = []
if n == 1:
  tri.append(int(input()))
  print(*tri)
else:
  for i in range(n):
    ip = list(map(int, input().split()))
    tri.append(ip)
  
  tri[1][0] += tri[0][0]
  tri[1][1] += tri[0][0]
  for i in range(2, n):
    tri[i][0] += tri[i-1][0]
    tri[i][i] += tri[i-1][i-1]
    # tri[i][1]~ tri[i][i-1] 까지 계산
    for j in range(1, i):
      tri[i][j] += max(tri[i-1][j-1], tri[i-1][j])
  print(max(tri[n-1]))