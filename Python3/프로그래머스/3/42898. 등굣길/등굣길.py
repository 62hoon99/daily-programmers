def solution(m, n, puddles):
    answer = 0
    dp = []
    
    puddles_set = set()
    for p_x, p_y in puddles:
        puddles_set.add((p_y - 1, p_x - 1))
        
    for i in range(n):
        dp.append([0] * m)
    for i in range(m):
        if (0,i) in puddles_set:
            break
        dp[0][i] = 1
    for i in range(n):
        if (i,0) in puddles_set:
            break
        dp[i][0] = 1
    
    for i in range(1, n):
        for j in range(1, m):
            if (i, j) in puddles_set:
                continue
                
            left = dp[i][j-1]
            up = dp[i-1][j]
            
            dp[i][j] = (left + up) % 1000000007

    return dp[n - 1][m - 1]