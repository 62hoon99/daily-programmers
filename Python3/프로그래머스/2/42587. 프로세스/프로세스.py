from collections import deque
import heapq

def solution(priorities, location):
    answer = 0
    
    heap = []
    q = deque()
    for i in range(len(priorities)):
        heapq.heappush(heap, -priorities[i])
        q.append((priorities[i], i))
    
    while len(q) > 0 and len(heap) > 0:
        p, l = q.popleft()
        if heap[0] == -1 * p:
            answer += 1
            heapq.heappop(heap)
            if location == l:
                return answer
        else:
            q.append((p, l))
        
    return answer