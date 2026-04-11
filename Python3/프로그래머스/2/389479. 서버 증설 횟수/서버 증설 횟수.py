from collections import deque

def solution(players, m, k):
    answer = 0
    
    # 큐에 서버가 종료되는 시간 입력
    q = deque()
    
    for i in range(len(players)):
        p = players[i]
        while len(q) > 0 and q[0] <= i:
            q.popleft()

        # 추가 증설이 필요한 경우
        if len(q) < p // m:
            # 추가 증설 필요 대수
            additional_server = p // m - len(q)
            
            for _ in range(additional_server):
                answer += 1
                q.append(i + k)
    
    return answer