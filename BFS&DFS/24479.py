import sys
def dfs(t):
    global cnt
    stack = [t]
    while stack:
        k = stack.pop()
        if visited[k]:
            continue
        visited[k] = cnt
        cnt += 1
        line[k].sort()
        for l in reversed(line[k]): ## reverse해서 넣는게 핵심
            if not visited[l]:
                stack.append(l)

N, M, R = map(int, sys.stdin.readline().split())

visited = [0]*(N+1)
cnt = 1
line = [[]for _ in range(N+1)]
for _ in range(M):
    s,e = map(int, sys.stdin.readline().split())
    line[s].append(e)
    line[e].append(s)

dfs(R)

for i in range(1, N+1):
    print(visited[i])