N = int(input())
num = list(map(int, input().split()))
op = list(map(int, input().split()))  # +, -, *, //


maximum = -1e9
minimum = 1e9


def dfs(depth, total, plus, minus, mutiple, divide):
    global maximum, minimum
    if depth == N:
        maximum = max(total, maximum)
        minimum = min(total, minimum)
        return
    if plus:
        dfs(depth+1, total + num[depth], plus-1,  minus, mutiple, divide)
    if minus:
        dfs(depth+1, total - num[depth], plus,  minus-1, mutiple, divide)
    if mutiple:
        dfs(depth+1, total * num[depth], plus,  minus, mutiple-1, divide)
    if divide:
        dfs(depth+1, int(total / num[depth]), plus,  minus, mutiple, divide -1)
        
dfs(1, num[0] ,op[0],op[1],op[2],op[3])
print(maximum)
print(minimum)