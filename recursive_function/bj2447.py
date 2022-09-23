n = int(input())

def star(l):
    if l == 3:
        return ['***','* *','***']
    arr = star(l//3) # 프렉탈 느낌으로 제일 작은 패턴부터 점점 확장
    stars = []

    for i in arr:
        stars.append(i*3)
    for i in arr:
        stars.append(i+' '*(l//3)+i)
    for i in arr:
        stars.append(i*3)
    return stars

print('\n'.join(star(n)))