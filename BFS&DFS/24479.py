import sys
sys.setrecursionlimit(150000)
def dfs(t):
    global cnt
    visited[t] = cnt
    line[t].sort()
    for i in line[t]:
        if not visited[i]:
            cnt += 1
            dfs(i)

N, M, R = map(int, input().split())

visited = [0]*(N+1)
cnt = 1
line = [[]for _ in range(N+1)]
for _ in range(M):
    s,e = map(int, input().split())
    line[s].append(e)
    line[e].append(s)

dfs(R)

for i in range(1, N+1):
    print(visited[i])