from collections import deque


test_case = int(input())

ans = []
for _ in range(test_case):
  documents, ord = map(int, input().split())
  priorty = deque((map(int, input().split())))
  cnt = 0
  idx = ord
  if documents == 1:
    ans.append(1)
  else:
    ord_value = priorty[ord]
    while max(priorty) != ord_value:
      try:
        if priorty[0] != max(priorty):
          priorty.append(priorty.popleft())
          if idx == 0:
            idx = len(priorty) - 1
          else:
            idx -= 1
        else:
          priorty.popleft()
          if idx == 0:
            idx = len(priorty) -1
          else:
            idx -= 1
          cnt += 1
      except Exception:
        break
    priorty = list(priorty)
    if idx > 0:
      if (priorty.count(max(priorty)) == 1 or max(priorty[:idx]) < max(priorty)):
        idx = 0
      else:
        cnt += priorty[:idx].count(max(priorty))
        idx = 0
    ans.append(cnt + idx + 1)
for i in ans:
  print(i)