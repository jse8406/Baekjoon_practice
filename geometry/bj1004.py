import math
case = int(input())
ans = []
for i in range(case):
    x1, y1, x2, y2 = map(int, input().split())
    n = int(input())
    count = 0
    for i in range(n):
        cx, cy, r = map(int, input().split())
        start_dis = math.sqrt((x1-cx)**2 + (y1-cy)**2)
        end_dis = math.sqrt((x2-cx)**2 + (y2-cy)**2)
        if start_dis < r and end_dis > r: 
            count += 1
        elif start_dis > r and end_dis < r: 
            count += 1
    ans.append(count)
for i in ans:
    print(i)
