def solution(routes):
    answer = 0

    l = list()
    for r in routes:
        l.append((r[1], r[0]))
    l.sort()
    
    pre_camera = -30001
    
    for elem in l:
        start = elem[1]
        end = elem[0]
        if pre_camera < start:
            answer += 1
            pre_camera = end
        
    return answer