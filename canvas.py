import heapq

case = int(input())
for _ in range(case):
  cost = 0
  temp = []
  data_len = int(input())
  data = list(map(int, input().split()))
  for i in range(data_len):
    heapq.heappush(temp, data[i])
  while len(temp) > 1:
    a = heapq.heappop(temp)
    b = heapq.heappop(temp)
    cost += a + b
    heapq.heappush(temp, a+b)
  print(cost)