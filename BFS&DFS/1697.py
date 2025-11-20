# 지역변수로 answer을 함수 안에 구현해놓고 +1을 각 경우마다 다 해보고 답이 나오면 answer return하고 끝?
N, K = map(int, input().split())
from collections import deque


def BFS(N,K):
    answer = 0
    visited = [False] * 100001
    q = deque()
    q.append(N)
    visited[N] = True
    while True:
        tmp = []
        while q:
            cur_pos = q.popleft()
            if cur_pos == K:
                return answer
            for next_pos in [cur_pos - 1, cur_pos + 1, cur_pos * 2]:
                if 0 <= next_pos <= 100000 and not visited[next_pos]:
                    tmp.append(next_pos)
                    visited[next_pos] = True
        q.extend(tmp)
        answer += 1
print(BFS(N,K))


