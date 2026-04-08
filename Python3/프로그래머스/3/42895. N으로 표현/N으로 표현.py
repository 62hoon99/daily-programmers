def solution(N, number):
    # dp[i] = N을 i번 사용해서 만들 수 있는 숫자 집합
    dp = [set() for _ in range(9)]
    
    for i in range(1, 9):
        # 1. 이어붙인 숫자 (예: 5, 55, 555)
        num = int(str(N) * i)
        dp[i].add(num)
        
        # 2. 이전 결과 조합
        for j in range(1, i):
            for a in dp[j]:
                for b in dp[i - j]:
                    dp[i].add(a + b)
                    dp[i].add(a - b)
                    dp[i].add(a * b)
                    if b != 0:
                        dp[i].add(a // b)
        
        # 3. 목표값 체크
        if number in dp[i]:
            return i
    
    return -1