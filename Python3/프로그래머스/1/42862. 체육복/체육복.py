def solution(n, lost, reserve):
    answer = 0
    
    s_l = set(lost) - set(reserve)
    s_r = set(reserve) - set(lost)

    s_l = sorted(list(s_l))
    s_r = sorted(list(s_r))
    
    pr = 0
    for s in s_l:
        while pr < len(s_r) and s + 1 >= s_r[pr]:
            if s_r[pr] < s - 1:
                pr += 1
            else:
                answer += 1
                pr += 1
                break
    
    return n - len(s_l) + answer