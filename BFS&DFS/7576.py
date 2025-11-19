N,M = map(int, input().split())

tomatoes = []

for _ in range(M):
    tomatoes.append([int(a) for a in input().split()])

from collections import deque

q = deque()
visited = [[0]*N for _ in range(M)]

for n in range(N):
    for m in range(M):
        if tomatoes[m][n] == 1:
            q.append((m,n))
            visited[m][n] = 1
        if tomatoes[m][n] == -1:
            # 토마토가 없는 곳도 방문했다고 가정해서 방문하지 못하게
            visited[m][n] = 1

answer = 0

while True:
    tmp = []
    while q:
        x,y = q.popleft()
        dx = [1,-1,0,0]
        dy = [0,0,1,-1]
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if 0<= nx <M and 0<= ny <N and not visited[nx][ny]:
                tmp.append((nx,ny))
                visited[nx][ny] = 1
    if tmp:
        q.extend(tmp)
        answer += 1
    else:
        break
flag = False
for v in visited:
    if 0 in v:
        flag = True

if flag:
    print(-1)
else:
    print(answer)