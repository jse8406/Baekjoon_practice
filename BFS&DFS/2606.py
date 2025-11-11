N = int(input())
M = int(input())

lines = [[] for _ in range(N+1)]

for _ in range(M):
    s,e = map(int, input().split())
    lines[s].append(e)
    lines[e].append(s)


visited = [0]*(N+1)
from collections import deque

answer = 0
q = deque([1])
visited[1] = 1
while q:
    k = q.popleft()
    for i in lines[k]:
        if not visited[i]:
            visited[i] = 1
            q.append(i)
            answer +=1
print(answer)