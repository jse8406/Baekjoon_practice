n = int(input())
bj_list = list(map(int, input().split()))
for i in range(1, n):
  bj_list[i] = max(bj_list[i], bj_list[i] + bj_list[i-1])
  print(max(bj_list))
