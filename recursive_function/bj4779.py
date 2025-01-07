def cut(result,start, end): #0 9라면 3부터5까지 공백 처리하고 0~2, 6~8에 대해서 칸토어 재귀귀
   # start가 0, end가 3이라면 0은 -, 1은 공백, 2는 - 이렇게 즉 start + end//3 <= < start + end//3 * 2까지 공백처리
    gap = end - start
    if gap == 1:
        return 
    else:
        for i in range(start+gap//3, start+(gap//3)*2):
           result[i] = ' '
        cut(result, start, start+gap//3)
        cut(result,start+gap//3*2, end)

while True:
    try :
        N = int(input())
        result = ['-']*(3**N)
        cut(result, 0,3**N)
        print(''.join(result))
    except : # EOF 발생시
        break # 종료