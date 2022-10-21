from typing import Deque
def left_len(a:int, deque:Deque):
  idx = deque.index(a)
  if idx == 0:
    return 0
  else:
    return len(list(deque)[:idx])
  
def right_len(a:int, deque:Deque):
  idx = deque.index(a)
  if idx == len(deque):
    return len(deque)
  else:
    return len(list(deque)[idx + 1:])
  
N, M = map(int, input().split())
pick_nums = Deque(map(int, input().split()))
n_list = Deque(i for i in range(1,N+1))
cnt = 0
while pick_nums:
  if left_len(pick_nums[0], n_list) - 1 <= right_len(pick_nums[0],n_list):
    while pick_nums[0] != n_list[0]:
      n_list.append(n_list.popleft())
      cnt += 1
    pick_nums.popleft()
    n_list.popleft()
  else:
    while pick_nums[0] != n_list[0]:
      n_list.appendleft(n_list.pop())
      cnt += 1
    pick_nums.popleft()
    n_list.popleft()
print(cnt)