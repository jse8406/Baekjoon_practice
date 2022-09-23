from itertools import combinations
from tracemalloc import start

n = int(input())
board = []
for i in range(n):
    a = list(map(int, input().split()))
    board.append(a)
member = [i for i in range(n)]
team_num = len(member)//2 # 한 팀의 멤버 수
teams = list(combinations(member, team_num))
team_start = teams[:len(teams)//2] # start 팀 구성 경우의수
team_link = teams[-1:len(teams)//2-1:-1] # link 팀 구성 경우의수

min_gap = 10000 # 최소 차이 저장 변수

for i in range(len(teams)//2):
    team = team_start[i]
    start_stat = 0
    for j in range(team_num):
        member = team[j]
        for k in team:
            start_stat += board[member][k]
    team = team_link[i]
    link_stat = 0
    for j in range(team_num):
        member = team[j]
        for k in team:
            link_stat += board[member][k]
    min_gap = min(min_gap, abs(start_stat - link_stat))
            
print(min_gap)