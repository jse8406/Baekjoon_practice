n = int(input())
m = int(input())
li = [i for i in range(n,m+1)] # elememt count = m-n 
sosoo = []
for i in range(m-n+1):
    count = 0
    for x in range(1, li[i]+1):
        if li[i]%x == 0:               
            count += 1
            if count > 2:
                break
    if count == 2: # 1 and itself
        sosoo.append(li[i])

if len(sosoo) == 0:
    print(-1)
else:
    print(sum(sosoo))
    print(min(sosoo))