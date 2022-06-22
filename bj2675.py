a = int(input())
for i in range(a):
    new_list = []
    str = input().split()
    str_list = list(str[1])
    for i in str_list:
        new_list += int(str[0])*i
        new_list = ''.join(new_list) #리스트 공백없이 문자열하나로 합치기
    print(new_list, end="\n")
         