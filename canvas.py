a = [1,2,3,4]
from collections import deque

b = deque(a)
print(b.popleft())
print(b)
