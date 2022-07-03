def isprime(num):
    if num == 1:
        return False
    else:
        eratos = [1]
        for i in range(2, int(num**0.5)+1): # 인수분해를 생각했을때 제곱근 기점으로 
            if num%i == 0:                  # 인수가 대칭이므로 그 전까지만 확인해도 똑같다
                return False
        return True
all_list = list(range(2,123456*2))
sosoo_list = []
for i in all_list:
    if isprime(i):
        sosoo_list.append(i)
input_list= []
while True:
    count = 0
    n = int(input())
    if n == 0:
        break
    else:
        input_list.append(n)   
for j in range(len(input_list)):
    count = 0
    for i in sosoo_list:
        if input_list[j]<i<2*input_list[j]+1:
            count+=1
    print(count)
    
    # 입력값의 범위 내에서 소수를 미리 추려내 다른 리스트에 저장한 후 그 적어진 값
    # 들과 비교하면 시간초과가 나지 않는다 cf: 에라토스테네스의 체