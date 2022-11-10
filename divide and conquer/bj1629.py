# 나머지 끼리의 곱을 다시 나누면 된다
# 나머지 분배 법칙 :
# (A x B) % C = (A % C) * (B % C) % C
import sys
A,B,C = map(int,sys.stdin.readline().split())

def dac(a,b,c):
  if b == 1:
    return a % c
  else:
    if b % 2 == 0:
      return (dac(a,b//2,c)**2)%c
    else:
      return ((dac(a,b//2,c)**2)*a)%c
print(dac(A,B,C))