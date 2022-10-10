# # 교차하는 전깃줄의 인덱스를 해당dp 인덱스에 저장, 가장 긴 배열을 지우고 지운 배열의 인덱스를 나머지 dp 배열 인덱스에서 삭제하면서 cnt값 1씩 증가, dp가 empty해질때까지 반복 후 cnt 출력

# line_num = int(input())
# lines = []
# dp = []

# for i in range(line_num):
#   line = list(map(int, input().split()))
#   lines.append(line)
# for i in range(line_num):
#   spare = []
#   for j in range(line_num):
#     if (lines[i][0] < lines[j][0] and lines[i][1] > lines[j][1]) or (lines[i][0] > lines[j][0] and lines[i][1] < lines[j][1]):
#       spare.append(j)
#   dp.append(spare)
# max_len = 0
# for i in range(line_num):
#   max_len = max(max_len, len(dp[i]))
# for i in range(line_num):
#   if len(dp[i]) == max_len:
#     idx = i
#   break
# dp[idx] = ["Delete"]
# while idx not in dp:
#   dp.remove(idx)
# print(dp)         # [3] [2] 남았을 때 [delete]때문에 오류가 날 것 같다.
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 첫 번째 풀이로 풀면 시간과 공간 복잡도가 너무 크다. 이를 어떻게 하면 더 효율적으로 풀 수 있는지 알아내야한다. 여기서 구하고자 하는 것은 최소의 전깃줄을 제거하여 전깃줄이 서로 안겹치게 하는 것.
# 전깃줄이 안겹치려면 x,y값이 그 전 전깃줄의 값보다 증가하여야한다(오름차순 정렬 되어 있을 경우) 이 떄 최소의 전깃줄을 제거하면 최대의 전깃줄이 남을 것이다. 따라서 안겹치는 최대의 남는 전깃줄을 구하려면
# x를 기준으로 정렬한 전깃줄에서 y에서 가장 긴 오름차순 배열을 찾으면 된다.

line_num = int(input())
lines = []
dp = [0] * line_num
for i in range(line_num):
  line = list(map(int, input().split()))
  lines.append(line)
lines.sort()
for i in range(line_num):
  for j in range(i):
    if lines[i][1] > lines[j][1] and dp[j] > dp[i]:
      dp[i] = dp[j]
  dp[i] += 1
print(line_num - max(dp))