def solution(mats, park):
    mats.sort(reverse = True)
    width = len(park[0])  # 8 
    height = len(park)  # 6
    answer = 0
    mats_count = len(mats)
    for i in range(height):
        for j in range(width):
            if park[i][j] == "-1":
                for index in range(mats_count):
                    error = 0
                    length = mats[index]
                    if length + i <= height and length + j <= width: # index 에러 안나는지 체크   
                        for h in range(length):
                            for w in range(length):
                                if park[i+h][j+w] != "-1":
                                    error += 1
                        if error == 0:
                            answer = max(length, answer)
    if answer == 0:
        return -1
    else:
        return answer
                            
print(solution([8,5,7],[["A", "A", "-1", "B", "B", "B", "B", "-1"], ["A", "A", "-1", "B", "B", "B", "B", "-1"], ["-1", "-1", "-1", "-1", "-1", "-1", "-1", "-1"], ["D", "D", "-1", "-1", "-1", "-1", "E", "-1"], ["D", "D", "-1", "-1", "-1", "-1", "-1", "F"], ["D", "D", "-1", "-1", "-1", "-1", "E", "-1"]] ))