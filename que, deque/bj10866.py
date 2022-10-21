import sys
from typing import Deque
input=sys.stdin.readline
deque = Deque()
N = int(input())
for i in range(N):
  ask = list(input().split())
  if ask[0] == "push_front":
    deque.appendleft(ask[1])
  if ask[0] == "push_back":
    deque.append(ask[1])
  if ask[0] == "pop_front":
    if not deque:
      print("-1")
    else:
      print(deque.popleft())
  if ask[0] == "pop_back":
    if not deque:
      print("-1")
    else:
      print(deque.pop())
  if ask[0] == "size":
    print(len(deque))
  if ask[0] == "empty":
    if not deque:
      print("1")
    else:
      print("0")
  if ask[0] == "front":
    if not deque:
      print("-1")
    else:
      print(deque[0])
  if ask[0] == "back":
    if not deque:
      print("-1")
    else:
      print(deque[-1])