def gcd(a,b): # 유클리드 호제법 시간복잡도 O(n)
    big = max(a,b)
    small = min(a,b)
    if big % small == 0:
        return small
    else:
        return gcd(small, big%small)
a,b = map(int, input().split())
print(gcd(a,b))
print(a*b//gcd(a,b)) # lcm은 두 수의 곱을 최대공약수로 나눈 것과 같다