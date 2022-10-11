# str1 = input()
# str2 = input()
# min_len = min(len(str1), len(str2))
# str1_len = len(str1)
# dp = [0] * str1_len
# for i in str2:
#   for j in range(str1_len):
#     if i == str1[j]:
#       dp[j] = max(dp[:j+1]) + 1
# print(min(max(dp), min_len))

        # 틀린 내 코드

# https://velog.io/@emplam27/%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-%EA%B7%B8%EB%A6%BC%EC%9C%BC%EB%A1%9C-%EC%95%8C%EC%95%84%EB%B3%B4%EB%8A%94-LCS-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-Longest-Common-Substring%EC%99%80-Longest-Common-Subsequence#%EC%B5%9C%EC%9E%A5-%EA%B3%B5%ED%86%B5-%EB%B6%80%EB%B6%84%EC%88%98%EC%97%B4longest-common-subsequence-%EA%B8%B8%EC%9D%B4-%EA%B5%AC%ED%95%98%EA%B8%B0

# LCS에 대해서 설명이 아주 잘 되어있다.

str1 = input()
str2 = input()

str1_len = len(str1)
dp = [0] * (str1_len + 1)
for i in str2:
  cnt = 0
  for j in range(str1_len):
    if cnt < dp[j]:
      cnt = dp[j]
    elif i == str1[j]:
      dp[j] = cnt + 1
  print(dp)
print(max(dp))