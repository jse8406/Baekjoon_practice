case = int(input())
for i in range(case):
    k = int(input()) #층 0층부터있다
    n = int(input()) #호 1호부터있다
    people = []
    for i in range(n):
        people.append(i+1)
    for j in range(k):
        for i in range(1,n):
            people[i] += people[i-1]
    print(people[n-1])