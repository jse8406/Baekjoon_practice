N = int(input())
house_cost = []
for i in range(N):
  ip = list(map(int, input().split()))
  house_cost.append(ip)
for i in range(1, N):
  house_cost[i][0] = min(house_cost[i-1][1], house_cost[i-1][2]) + house_cost[i][0]
  house_cost[i][1] = min(house_cost[i-1][0], house_cost[i-1][2]) + house_cost[i][1]
  house_cost[i][2] = min(house_cost[i-1][0], house_cost[i-1][1]) + house_cost[i][2]
  
print(min(house_cost[N-1]))