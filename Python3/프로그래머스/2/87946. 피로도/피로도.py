def solution(k, dungeons):
    answer = -1
    
    def rcs(current, c_set, c_k, count):
        if (c_k < current[0]) or (current in c_set) or (c_k - current[1] < 0):
            return count
        
        next_k = c_k - current[1]
        
        c_set.add(current)
        
        result = count
        
        for d in dungeons:
            r_r = rcs((d[0], d[1]), c_set, next_k, count + 1)
            result = max(r_r, result)
        
        c_set.remove(current)
        
        return result

    for d in dungeons:
        r_r = rcs((d[0], d[1]), set(), k, 0)
        answer = max(r_r, answer)
    
    return answer