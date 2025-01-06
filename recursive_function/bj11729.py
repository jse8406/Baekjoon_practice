N = int(input())

def hanoi(n, start, end, spare):
    if n == 1:
        print(start, end)
        return
    else:
        hanoi(n-1, start, spare, end)
        print(start, end)
        hanoi(n-1,spare, end, start)

print(2**N-1)
hanoi(N, 1, 3, 2)