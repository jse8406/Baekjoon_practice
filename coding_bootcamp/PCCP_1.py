def solution(video_len, pos, op_start, op_end, commands):
    video_min, video_sec = map(int, video_len.split(":"))
    pos_min, pos_sec = map(int, pos.split(":"))
    ops_min, ops_sec = map(int,op_start.split(":"))
    ope_min, ope_sec = map(int, op_end.split(":"))
    # 시간을 35:00 이면 3500으로 변형 후 값 비교
    video = video_min*100 + video_sec
    op_s = ops_min*100 + ops_sec
    op_e = ope_min*100 + ope_sec
    cur_pos = pos_min*100 + pos_sec
    
    for command in commands:
        # pos가 오픈닝에 포함되어있는지 항상 먼저 체크
        if op_s <= cur_pos < op_e:
            cur_pos = op_e
         
        if command == "next":
            cur_pos += 10
            if cur_pos % 100 > 59:
                cur_pos = cur_pos + 40
        if command == "prev":
            cur_pos -= 10
            if cur_pos < 0:
                cur_pos = 0
            if cur_pos % 100 > 59:
                cur_pos = cur_pos - 40
    # 34:02에서 10초 빼면 33:52가 되야함. 그런데 지금은 3392가 됨

        if cur_pos > video:
            cur_pos = video

    # 명령어 다 수행 후 마지막에 한번 더 체크
    if op_s <= cur_pos < op_e:
            cur_pos = op_e
    
    # cur_pos가 "mm:ss"의 형식이 되도록 변형
    cur_pos = str(cur_pos)
    while len(cur_pos) != 4:
        cur_pos = '0' + cur_pos
    cur_pos = cur_pos[:2] + ":" + cur_pos[2:]
    return cur_pos

print(solution("07:22","04:05","00:15","04:07",["next"]))