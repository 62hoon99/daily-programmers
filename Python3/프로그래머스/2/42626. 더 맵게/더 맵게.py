import heapq

def solution(scoville, K):
    answer = 0
    food = []
    
    for s in scoville:
        heapq.heappush(food, s)

    while food[0] < K:
        if len(food) < 2:
            return -1
        f1 = heapq.heappop(food)
        f2 = heapq.heappop(food)
        heapq.heappush(food, f1 + (f2 * 2))
        answer += 1
    
    return answer