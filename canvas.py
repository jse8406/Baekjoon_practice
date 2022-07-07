import sys
input = sys.stdin.readline
n = int(input())
point_list = []
for i in range(n):
    point_list.append(list(map(int, input().split())))

sorted_list = sorted(point_list)

for i in range(n):
    print(sorted_list[i][0], sorted_list[i][1])               
                 