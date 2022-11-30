import sys
input = sys.stdin.readline

n, k = map(int,(input().split()))
p = 1000000007

fact = [1 for _ in range(n+1)]


for i in range(2, n+1):
  fact[i] = fact[i-1] * i % p
    
def square(n, k):
  if k == 0:
    return 1
  elif k == 1:
    return n
  
  tmp = square(n, k//2)
  if k % 2:
    return tmp * tmp * n % p
  else:
    return tmp * tmp % p
  
top = fact[n]
bot = fact[n-k] * fact[k] % p

print((top%p) * (square(bot, p-2)%p) %p)

# 페르마의 소정리, 모듈러 연산의 곱셈 분배 법칙, dp
# a^(p-2) % p = 1/a % p 
# (a * b) % p = (a % p * b % p) % p
 