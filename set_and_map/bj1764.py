n,m = map(int, input().split())
no_listened = []
no_heard = []
no_listened_heard = {}
for i in range(n):
    no_listened.append(input())
    if no_listened[i] not in no_listened_heard:
        no_listened_heard[no_listened[i]] = 1
for i in range(m):
    no_heard.append(input())
    if no_heard[i] not in no_listened_heard:
        no_listened_heard[no_heard[i]] = 1
    else:
        no_listened_heard[no_heard[i]] += 1
count = 0
ans = []
for i in no_listened_heard:
    if no_listened_heard[i] == 2:
        count += 1
        ans.append(i)
ans.sort()
print(count)
for i in ans:
    print(i)