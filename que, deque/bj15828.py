from queue import Queue
import sys
input = sys.stdin.readline
router = Queue()

N = int(input())
while True:
  a = int(input())
  if a == 0:
    router.get()
  elif a == -1:
    break
  else:
    if router.qsize() < N:
      router.put(a)

if router.empty():
  print('empty')
else:
  print(*router.queue)