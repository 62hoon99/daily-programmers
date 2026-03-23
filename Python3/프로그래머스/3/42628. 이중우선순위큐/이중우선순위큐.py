import heapq
from collections import defaultdict

def solution(operations):
    max_q = []
    min_q = []
    counter = defaultdict(int)
    
    for o in operations:
        if o[0] == "I":
            num = int(o[2:])
            counter[num] = counter[num] + 1
            heapq.heappush(max_q, -num)
            heapq.heappush(min_q, num)
        if o == "D -1":
            while len(min_q) > 0:
                min_num = heapq.heappop(min_q)
                if counter[min_num] > 0:
                    counter[min_num] = counter[min_num] - 1
                    break
        if o == "D 1":
            while len(max_q) > 0:
                max_num = -1 * heapq.heappop(max_q)
                if counter[max_num] > 0:
                    counter[max_num] = counter[max_num] - 1
                    break
    
    min_num = 999999999
    max_num = -999999999
    
    for k, v in counter.items():
        if v > 0:
            min_num = min(min_num, k)
            max_num = max(max_num, k)
    
    if max_num == -999999999 and min_num == 999999999:
        return [0, 0]
    return [max_num, min_num]