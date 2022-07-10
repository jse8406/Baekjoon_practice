from sys import stdin
def input():
    return stdin.readline().rstrip()
n,m = map(int, input().split())
dogam = {}
dogam_reverse = {}
for i in range(n):
    a = input()
    dogam[a] = i+1
    dogam_reverse[i+1] = a
for i in range(m):
    a = input()
    if a.isdigit():
        print(dogam_reverse[int(a)])
    else:
        print(dogam[a])
