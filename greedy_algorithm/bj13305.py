n = int(input())

distance = list(map(int, input().split()))
cost = list(map(int, input().split()))

ans = distance[0] * cost[0]
min_cost = cost[0]
for i in range(1, n-1):
    if cost[i] < min_cost:
        min_cost = cost[i]
    ans += min_cost * distance[i]

print(ans)