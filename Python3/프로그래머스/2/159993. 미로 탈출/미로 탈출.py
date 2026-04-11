from collections import deque

def solution(maps):
    answer = 0
    start_at = None
    exit_at = None
    lever_at = None
    
    dirs = [(-1,0), (1,0), (0,-1), (0,1)]
    
    for i in range(len(maps)):
        for j in range(len(maps[i])):
            if maps[i][j] == 'S':
                start_at = (i, j)
            if maps[i][j] == 'L':
                lever_at = (i, j)
            if maps[i][j] == 'E':
                exit_at = (i, j)
    
    # 시작 -> 레버
    q = deque()
    visited_1 = set()
    q.append((start_at[0], start_at[1], 0))
    result_1 = 0
    visited_1.add((start_at[0], start_at[1]))
    
    while len(q) > 0:
        y, x, depth = q.popleft()
        
        for d_y, d_x in dirs:
            to_y = y + d_y
            to_x = x + d_x
            if to_x > -1 and to_x < len(maps[0]) and to_y > -1 and len(maps) > to_y:
                if maps[to_y][to_x] == 'L':
                    result_1 = depth + 1
                    break
                if maps[to_y][to_x] != 'X' and (to_y, to_x) not in visited_1:
                    q.append((to_y, to_x, depth + 1))
                    visited_1.add((to_y, to_x))
    
        if result_1 > 0:
            break
    if result_1 == 0:
        return -1
    
    # 레버 -> 출구
    q = deque()
    visited_2 = set()
    q.append((lever_at[0], lever_at[1], 0))
    result_2 = 0
    visited_2.add((lever_at[0], lever_at[1]))
        
    while len(q) > 0:
        y, x, depth = q.popleft()
        visited_2.add((y,x))
        
        for d_y, d_x in dirs:
            to_y = y + d_y
            to_x = x + d_x
            if to_x > -1 and to_x < len(maps[0]) and to_y > -1 and len(maps) > to_y:
                if maps[to_y][to_x] == 'E':
                    result_2 = depth + 1
                    break
                if maps[to_y][to_x] != 'X' and (to_y, to_x) not in visited_2:
                    q.append((to_y, to_x, depth + 1))
                    visited_2.add((to_y, to_x))
        
        if result_2 > 0:
            break
    
    if result_2 == 0:
        return -1
    
    return result_1 + result_2