import sys
input = sys.stdin.readline

n,c = map(int, input().split())
houses = [int(input()) for _ in range(n)]
houses.sort()
start = 1 #최소 거리
end = houses[n-1] - houses[0] #최대 거리

ans = 0
if c == 2:
  print(houses[n-1] - houses[0]) #집 3개면 처음과 끝집 사이의 거리가 답
else:
  while start < end:
    mid = (start + end) // 2
    count = 1 #last house에 하나 놓고 시작하기 때문에 1부터 시작
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
  
  # 핵심 : pivot을 두 집 사이의 거리로 잡고(정답의 후보를 정해놓고) 그 때의 공유기 수를 계산하며 pivot을 조절해 나간다.