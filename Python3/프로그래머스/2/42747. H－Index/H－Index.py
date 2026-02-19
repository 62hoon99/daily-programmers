def solution(citations):
    answer = 1
    
    citations.sort(reverse=True)
    
    if citations[0] == 0:
        return 0
    
    for i in range(len(citations)):
        if citations[i] < i + 1:
            break
        answer = i + 1
    
    return answer