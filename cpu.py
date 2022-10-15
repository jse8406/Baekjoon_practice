import collections

tasks = ["A","A","A","B","C","D"]
n = 2
counter = collections.Counter(tasks)
result = 0
while True:
  sub_count = 0
  # 개수 순 추출
  for task, _ in counter.most_common(n+1):
    sub_count += 1
    result += 1
    print(sub_count, result, 'THis')
    
    counter.subtract(task)
    counter += collections.Counter() # 이게 0에서 멈추게 하는 기능을 한다.
  if not counter:
    break
  result += n - sub_count + 1
  print(result)
print(result)