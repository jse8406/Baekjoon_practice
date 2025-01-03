N = int(input())

def star(n):
    if n == 3:
        return ['***', '* *', '***']
    arr = star(n//3)
    stars = []
    
    for i in arr:
        stars.append(i*3)
    for i in arr:
        stars.append(i+' '*(n//3)+i)
    for i in arr:
        stars.append(i*3)
    return stars
    
print('\n'.join(star(N)))

# stars에 작은 패턴부터 저장해놓고 그걸 다시 가져와서 * 연산으로 점점 부풀려 나가는 느낌낌