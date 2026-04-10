def solution(distance, rocks, n):
    answer = 0
    
    # 0, 2, 11, 14, 17, 21, 25
    # 사이거리: 2, 9, 3, 3, 4, 4
    
    left = 1
    right = distance
    rocks.append(0)
    rocks.append(distance)
    rocks.sort()
    
    while left <= right:
        mid = (left + right) // 2
        
        result = 0
        dis = 0
        for i in range(1, len(rocks)):
            if rocks[i] - rocks[i - 1] + dis >= mid:
                dis = 0
            else:
                result += 1
                dis += rocks[i] - rocks[i - 1]
        
        # print(left)
        # print(right)
        # print(result)
        # print(mid)
        # print()
    
        if result > n:
            right = mid - 1
        else:
            answer = mid
            left = mid + 1
    
    return answer