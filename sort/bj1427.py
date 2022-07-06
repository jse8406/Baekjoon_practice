n = input()
li = []
for i in n:
    li.append(int(i))
li.sort(reverse=True)
for i in li:
    print(i, end="")