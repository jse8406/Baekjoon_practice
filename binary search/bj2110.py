import sys
input = sys.stdin.readline

n,c = map(int, input().split())
houses = [int(input()) for _ in range(n)]
houses.sort()
start = 1
end = houses[n-1] - houses[0]

ans = 0
if c == 2:
  print(houses[n-1] - houses[0])
else:
  while start < end:
    mid = (start + end) // 2
    count = 1
    last_house = houses[0]
    
    for i in range(n):
      if houses[i] - last_house >= mid:
        count += 1
        last_house = houses[i]
    if count >= c:
      ans = mid
      start = mid + 1
    elif count < c:
      end = mid
  print(ans)