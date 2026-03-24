def solution(brown, yellow):
    answer = []
    
    # brown + yellow = return[0] * return[1]
    # (return[0] - 2) * (return[1] - 2) = yellow
    
    total = brown + yellow
    
    for i in range(3, total):
        if total % i == 0:
            right = i
            left = total // i
            if (left - 2) * (right - 2) == yellow:
                return [left, right]
    
    return answer