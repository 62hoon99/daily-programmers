from collections import deque, Counter, defaultdict
import heapq

def solution(participant, completion):
    answer = ''
    
    counter = Counter(participant)
    
    for c in completion:
        counter[c] -= 1
    
    for k, v in counter.items():
        if v > 0:
            answer = k
            break
    
    return answer