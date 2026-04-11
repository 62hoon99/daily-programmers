import heapq

def solution(n, k, enemy):
    if k >= len(enemy):
        return len(enemy)
    
    answer = 0
    
    heap = []
    
    for i in range(len(enemy)):
        heapq.heappush(heap, -1 * enemy[i])
        
        if n >= enemy[i]:
            n -= enemy[i]
        elif k > 0:
            max_enemy = -1 * heapq.heappop(heap)
            n += max_enemy
            n -= enemy[i]
            k -= 1
        else:
            break
        
        answer += 1
    
    return answer