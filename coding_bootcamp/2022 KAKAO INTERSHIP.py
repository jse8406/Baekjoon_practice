# rt, cf, jm an
def solution(survey, choices):
    count = len(survey)
    dic = {'R':0, 'T':0, 'C':0, 'F':0, 'J':0, 'M':0, 'A':0, 'N':0}
    for i in range(count):
        first = survey[i][0]
        sec = survey[i][1]
        choice = choices[i]
        
        ## choice가 1~3이면 first가 3, 2, 1점 , 4는 아무것도없음, 5~7 이면 sec가 1, 2, 3점
        if choice == 1:
            dic[first] += 3
        elif choice == 2:
            dic[first] += 2
        elif choice == 3:
            dic[first] += 1
        elif choice == 4:
            pass
        elif choice == 5:
            dic[sec] += 1
        elif choice == 6:
            dic[sec] += 2
        elif choice == 7:
            dic[sec] += 3
            
        # 이렇게 반복문으로 계산한 값 dictionary에 누적한담에 rt, cf, jm, an 각각 2개씩 비교해서 더 큰 값 선택 후 리턴
    answer = ''
    keys_list = list(dic.keys())
    for i in range(0,8,2):
        if dic.get(keys_list[i]) > dic.get(keys_list[i+1]):
            answer += keys_list[i]
        elif dic.get(keys_list[i]) < dic.get(keys_list[i+1]):
            answer += keys_list[i+1]
        else:
            answer += min(keys_list[i],keys_list[i+1])
            
    return answer

print(solution(["AN", "CF", "MJ", "RT", "NA"],[5, 3, 2, 7, 5]))