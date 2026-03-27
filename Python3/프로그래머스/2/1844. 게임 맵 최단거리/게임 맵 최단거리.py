from collections import deque

def solution(maps):
    n, m = len(maps), len(maps[0])
    
    memory = [[-1] * m for _ in range(n)]
    queue = deque()
    
    queue.append((0, 0))
    memory[0][0] = 1
    pos = [(-1, 0), (1, 0), (0, 1), (0, -1)]
    
    while len(queue) > 0:
        left, right = queue.popleft()
        
        for lp, rp in pos:
            nl = left + lp
            nr = right + rp
            
            if nl > -1 and nl < n and nr > -1 and nr < m:
                if maps[nl][nr] == 1 and memory[nl][nr] == -1:
                    memory[nl][nr] = memory[left][right] + 1
                    queue.append((nl, nr))
        
    return memory[n - 1][m - 1]