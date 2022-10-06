n = int(input())
time_list = []
for i in range(n):
  start, end = map(int, input().split())
  time_list.append([start, end])
time_list.sort(key=lambda x: (x[1], x[0]))
ans = 1
end_time = time_list[0][1]
for i in range(1,n):
  if time_list[i][0] >= end_time:
    ans += 1
    end_time = time_list[i][1]
print(ans)