from collections import defaultdict

def solution(clothes):
    map = defaultdict(list)
    
    for c in clothes:
        map[c[1]].append(c[0])
    
    result = 1
    for k, v in map.items():
        result = result * (len(v) + 1)
    
    return result - 1