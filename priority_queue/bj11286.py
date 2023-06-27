import heapq # 최소 힙만 제공한다.
import sys
# 절댓값이 가장 작은... 결국 양수로 바꾼 후 최소 힙 이용한 뒤 양수로 바꾼 흔적이 있는 수는 다시 음수로 출력
N = int(input())
abs_heap_plus = []
abs_heap_minus = []
inp = []

for _ in range(N):
  a = int(sys.stdin.readline())
  inp.append(a)
  
for i in range(N):
  if inp[i] == 0:
    if not abs_heap_plus and not abs_heap_minus:
      print(0)
    elif not abs_heap_minus and abs_heap_plus:
      print(heapq.heappop(abs_heap_plus))
    elif not abs_heap_plus and abs_heap_minus:
      print(-1 * heapq.heappop(abs_heap_minus))
    else:
      min_plus = heapq.heappop(abs_heap_plus)
      min_minus = heapq.heappop(abs_heap_minus)
      if min_plus < min_minus:
        print(min_plus)
        heapq.heappush(abs_heap_minus, min_minus)
      else:
        print(-1*min_minus)
        heapq.heappush(abs_heap_plus, min_plus)
  else:
    if inp[i] > 0:
      heapq.heappush(abs_heap_plus, inp[i])
    else:
      heapq.heappush(abs_heap_minus, -1*inp[i])