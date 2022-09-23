def hansu(num):
    cnt = 0
    for i in range(1, num+1):
        num_list = list(map(int, str(i))) #각 자리 수를 리스트에 하나씩 저장
        if i <100:
            cnt += 1
        elif num_list[0]-num_list[1] == num_list[1]-num_list[2]:
            cnt += 1
    return cnt  #return ident 때문에 계속 잘못된 값이 리턴.
num = int(input())
print(hansu(num))


    