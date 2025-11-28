N, M = map(int, input().split())

map = []
for _ in range(N):
    m = input()
    map.append(m)

# 0,0에서 시작해서 N-1, M-1에 도착
# 0만 다닐 수 있고 1은 벽, 단 한 번은 꺨 수 있음
# 벽을 부쉈냐 안부쉈냐를 어떻게 저장할 것 인가?
from collections import deque
visited = [[[0]*2 for _ in range(M)] for _ in range(N)]
dx = [1,-1,0,0]
dy = [0,0,1,-1]
visited[0][0][0] = 1

def BFS(n,m, c):
    dq = deque()
    dq.append((n,m,c))
    while dq:
        x,y,c = dq.popleft()
        if x == N-1 and y == M-1:
            return visited[x][y][c]

        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0>nx or nx >=N or ny <0 or ny >= M:
                continue
            ## 벽을 만나면 c가 0이어야만 함, 벽은 visited 체크 안해도 되는 이유?
            if map[nx][ny] == '1' and c == 0:
                visited[nx][ny][1] = visited[x][y][0]+1
                dq.append((nx,ny,1))
            # 길이면 방문 안한지만 체크하면 됨
            elif map[nx][ny] == '0' and visited[nx][ny][c] == 0:
                visited[nx][ny][c] = visited[x][y][c]+1
                dq.append((nx,ny,c))
    return -1 
print(BFS(0,0,0))