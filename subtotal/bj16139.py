# S = input()
# q = int(input())
# str_len = len(S)
# for i in range(q):
#   sub_total = [0] * (str_len+1)
#   char, start, end = input().split()
#   start = int(start)
#   end = int(end)
#   for j in range(str_len):
#     if S[j] == char:
#       sub_total[j + 1] += 1
#     sub_total[j + 1] += sub_total[j]
#   print(sub_total[end+1] - sub_total[start])

import sys
input = sys.stdin.readline

name = input().strip()
n = int(input())
arr = [[0 for i in range(26)] for i in range(len(name))]
arr[0][ord(name[0]) - 97] = 1
for i in range(1, len(name)):
    arr[i][ord(name[i]) - 97] = 1
    for j in range(26):   # 상수 range for 문은 부담없이 써도 된다. 시간 복잡도가 상수다.
        arr[i][j] += arr[i - 1][j]
for i in range(n):
    a = input().split()
    if int(a[1]) > 0:
        res = arr[int(
            a[2])][ord(a[0]) - 97] - arr[int(a[1]) - 1][ord(a[0]) - 97]
    else:
        res = arr[int(a[2])][ord(a[0]) - 97]
    print(res)