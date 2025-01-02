n = int(input())
ans = 1
dance = ["ChongChong"]
for i in range(n):
    first, second = input().split(" ")
    if (first in dance and second not in dance):
        ans += 1
        dance.append(second)
    elif (first not in dance and second in dance):
        ans += 1
        dance.append(first)
print(ans)