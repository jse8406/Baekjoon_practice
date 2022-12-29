from queue import Queue
import inspect

class Node:
  def __init__(self, key = None) -> None:
    self.key = key
    self.next = None
  def __str__(self) -> str:
    return str(self.key)

a = Node(3)
b = Node(9)
c = Node(-1)

a.next = b
b.next = c

print(a.next.next)

a = inspect.getsource(Queue)
print(a)

que = Queue()

que.put(4)