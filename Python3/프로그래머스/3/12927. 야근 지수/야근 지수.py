def solution(n, works):
    answer = 0
    
    works.sort(reverse=True)

    while n > 0:
        max_v = works[0]
        
        if max_v == 0:
            break
        
        for i in range(len(works)):
            if works[i] == max_v:
                works[i] -= 1
                n -= 1
                
                if n == 0:
                    break
            else:
                break
    
    for w in works:
        answer += (w * w)
    
    return answer