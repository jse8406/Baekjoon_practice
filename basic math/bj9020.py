def isprime(num):
    if num == 1:
        return False
    elif num < 1:
        return False
    else:
        eratos = [1]
        for i in range(2, int(num**0.5)+1):
            if num%i == 0:                  
                return False
        return True

n = int(input())
input_list = []
for i in range(n):
    a = int(input())
    input_list.append(a)
M = max(input_list)
all_list = [i for i in range(M)]
sosoo_list = [] # 입력받은 값 중 제일 큰 수 까지의 소수들
for i in all_list:
    if isprime(i):
        sosoo_list.append(i)
for i in range(n):
    val_dif = max(input_list)
    for j in sosoo_list:
        if isprime(input_list[i] - j) and abs(input_list[i] - 2*j) < val_dif:
            ans1, ans2 = j, input_list[i] - j
            val_dif = abs(input_list[i] - 2*j)
    print(ans1, ans2)