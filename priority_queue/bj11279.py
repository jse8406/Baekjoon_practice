import heapq # 최소 힙만 제공한다.
import sys

N = int(input())
heap = []
inp = []
for _ in range(N):
  a = int(sys.stdin.readline())
  inp.append(a * -1)
for i in range(N):
  if inp[i] == 0:
    if not heap:
      print(0)
    else:
      print(-1 * heapq.heappop(heap))
  else:
    heapq.heappush(heap, inp[i])
  