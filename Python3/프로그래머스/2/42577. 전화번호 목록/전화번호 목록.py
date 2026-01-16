from collections import deque, defaultdict, Counter
import heapq

def solution(phone_book):
    answer = True
    
    d = defaultdict(set)
    for pb in phone_book:
        d[len(pb)].add(pb)
    
    for k, v in d.items():
        
        for pb in phone_book:
            if len(pb) > k and (pb[0:k] in v):
                return False
    
    return True