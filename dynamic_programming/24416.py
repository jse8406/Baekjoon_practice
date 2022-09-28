num = int(input())
def fib(n):
    if n == 1 or n == 2:
        fib.counter += 1
        return 1
    else:
        return fib(n-1) + fib(n-2)
    
def dynamic_fib(n):
    
    f[1],f[2] = 1,1
    for i in range(3,n+1):
        dynamic_fib.counter += 1
        f[i] = f[i-1] + f[i-2]
    return f[n]


fib.counter = 0
dynamic_fib.counter = 0
f = [0 for _ in range(41)]
fib(num)
dynamic_fib(num)
print(fib.counter, dynamic_fib.counter)