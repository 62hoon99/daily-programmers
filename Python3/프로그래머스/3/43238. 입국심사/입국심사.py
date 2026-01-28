def solution(n, times):
    answer = float('inf')
    times.sort()
    
    left = 1
    right = n * times[-1]

    while left <= right:
        mid = (left + right) // 2

        count = 0
        for t in times:
            count += mid // t
        
        if count >= n:
            answer = min(answer, mid)
            right = mid - 1
        else:
            left = mid + 1
    
    return answer