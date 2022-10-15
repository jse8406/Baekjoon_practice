# A = ["asd dfg", "qwe cvb"]
# print(A[0].split()[0])
def solution(id_list, report, k): # 유저 리스트, 이용자id 신고한 id , 정지 신고 횟수
    answer = []
    id_list_dict = {i:0 for i in id_list} # id 리스트 딕셔너리로 바꾸기
    stopped_id_list_dict = {i:0 for i in id_list}
    report_set = list(set(report)) # 중복 없애기
    for i in range(len(report_set)):
        id_list_dict[report_set[i].split()[1]] += 1 # 신고당한사람 신고횟수 저장
    stopped_user = []
    
    for i in id_list:
        if id_list_dict[i] >= k:
            stopped_user.append(i) # 신고횟수가 k 이상인 사람 정지 유저로 저장
            
    for i in stopped_user:
        for j in range(len(report_set)):      # 정지 유저를 신고한 사람이 받을
            if i == report_set[j].split()[1]: # 메일 수 저장
                stopped_id_list_dict[report_set[j].split()[0]] += 1
                break
    answer = list((stopped_id_list_dict.values()))
    
    return answer