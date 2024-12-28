def check_X(result, xs):
    X= result[0]
    Y = result[1]
    for x in xs:
        d_x = x[0]
        d_y = x[1] 
        if X == d_x and Y == d_y:
            return False
        elif X == d_x:
            if Y > d_y:
                return False
        elif Y == d_y:
            if X > d_x:
                return False
        else:
            return True        
            
                
        

def solution(park, routes):
    
    h = len(park)
    w = len(park[0])
    xs = []
    for i in range(h):
        for j in range(w):
            if park[i][j] == 'S':
                result = [i,j]
            elif park[i][j] == 'X':
                xs.append([i,j])
    # init start point            
    for route in routes:
        dir, dis = route.split(" ")
        dis = int(dis)
        origin_x = result[0]
        origin_y = result[1]
        if dir == "N":
            if result[0] - dis >= 0:
                result[0] = result[0] - dis
        elif dir == "S":
            if result[0] + dis < h:
                result[0] = result[0] + dis
        elif dir == "W":
            if result[1] + dis < w:
                result[1] = result[1] + dis
        else:
            if result[1] - dis >= 0:
                result[1] = result[1] - dis
        if check_X(result, xs):
            result[0], result[1] = origin_x, origin_y
                
    return result


print(solution(["SOO","OXX","OOO"]	, ["E 2","S 2","W 1"]))