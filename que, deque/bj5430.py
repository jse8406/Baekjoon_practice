
from collections import deque

test_case = int(input())
for _ in range(test_case):
  cnt = 0
  p = input()
  num_count = int(input())
  arr = input()
  arr = arr.replace('[', '')
  arr = arr.replace(']', '')
  arr = arr.replace(',',' ', num_count-1)
  arr = deque(list(map(int, arr.split())))
  if p.count('D') > len(arr):
    print('error')
  else:
    while p != p.replace('RR', ''):
      p = p.replace('RR', '')
    for char in p:
      if char == "R":
        cnt += 1 # reverse해야하는 문제지만 reverse를 하면 시간초과가 나는 아이러니, reverse없이 문제를 풀어야 시간초과가 나지 않는다.
      else:
        if cnt % 2 == 0:
          arr.popleft()
        else:
          arr.pop()
    if cnt % 2 == 1:
      arr.reverse()
    print('[', end='')
    cnt = 0
    for i in arr:
      cnt += 1
      if cnt != len(arr):
        print(i,end=',')
      else:
        print(i, end='')
    print(']')
    
    # deque의 장점: 양방향 pop의 시간복잡도가 O(1)이므로 사실상 reverse()는 시간복잡도만 키울뿐 사용할 필요가 굳이 없다.
