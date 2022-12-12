n = int(input())
sang = sorted(list(map(int, input().split())))
m = int(input())
card = list(map(int, input().split()))
ans = {}
for i in sang:
    if i in ans:
        ans[i] += 1
    else:
        ans[i] = 1
for i in card:
    if i in ans:
        print(ans[i], end=" ")
    else:
        print(0, end=" ")