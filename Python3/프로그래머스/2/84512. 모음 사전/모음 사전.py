def solution(word):
    answer = 0
    
    words = []
    
    def rcs(current, depth):
        if depth == 5:
            return
        
        for alp in ['A', 'E', 'I', 'O', 'U']:
            words.append(current + alp)
            rcs(current + alp, depth + 1)
    
    rcs("", 0)
    
    for w in words:
        answer += 1
        if word == w:
            return answer
    
    return answer