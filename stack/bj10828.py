import sys
input=sys.stdin.readline
def push(stack:list, val):
  stack.append(val)
  
def top(stack:list):
  if len(stack):
    return stack[-1]
  else:
    return -1

def size(stack:list):
  return len(stack)
  
def empty(stack:list):
  if len(stack) != 0:
    return 0
  else:
    return 1
  
def pop(stack:list):
  if empty(stack):
    return -1
  else:
    return stack.pop()
  
stack = []
N = int(input())
for i in range(N):
  ask = list(input().split())
  if ask[0] == "push":
    push(stack, ask[1])
    continue
  elif ask[0] == "top":
    print(top(stack))
    continue
  elif ask[0] == "size":
    print(size(stack))
    continue
  elif ask[0] == "empty":
    print(empty(stack))
    continue
  elif ask[0] == "pop":
    print(pop(stack))
    continue