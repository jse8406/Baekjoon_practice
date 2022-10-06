N = int(input())
P = list(map(int, input().split()))
P.sort(reverse=True)
ans = 0
for i in range(N):
  ans += sum(P[i:N])
print(ans)