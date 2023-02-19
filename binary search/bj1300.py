N = int(input())
k = int(input())

start, end = 1, N**2

while start <= end:
  idx = 0
  mid = (start + end) // 2 # mid는 임의의 수로 이 수가 몇 번째인지 이분 탐색으로 점점 좁혀나감
  for i in range(1,N+1):
    idx += min(N, mid // i)
  if idx >= k: # mid가 찾는 수보다 크다 
    ans = mid
    end = mid - 1
  else:
    start = mid + 1
print(ans)