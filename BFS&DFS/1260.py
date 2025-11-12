import sys
from collections import deque

v, e, s = map(int, sys.stdin.readline().split())
lines = [[] for _ in range(v+1)]

for _ in range(e):
    start, end = map(int ,sys.stdin.readline().split())
    lines[start].append(end)
    # 양방향으로 설정해두어야 하는거??
    # 최소 탐색이 아닌데 
    # lines[end].append(start)

def BFS(R):
    visited = [0]*(v+1)
    q = deque()
    q.append(R)
    answer = [R]
    visited[R] = 1

    while q:
        cur = q.popleft()
        for i in lines[cur]:
            if visited[i] == 0:
                q.append(i)
                answer.append(i)
                visited[i] = 1
    return answer

def DFS(R):
    visited = [0]*(v+1)
    stack = [R]
    answer = []

    while stack:
        cur = stack.pop()
        if not visited[cur]:
            visited[cur] = 1
            answer.append(cur)
            for i in reversed(lines[cur]):
                if not visited[i]:
                    stack.append(i)
    return answer        
answer_bfs = BFS(s)
answer_dfs = DFS(s)

print(*answer_dfs)
print(*answer_bfs)

