from collections import defaultdict
import heapq

def solution(genres, plays):
    answer = []
    
    g_dict = defaultdict(int)
    g_q = []
    
    for i in range(len(plays)):
        g_dict[genres[i]] = g_dict[genres[i]] + plays[i]
    for k, v in g_dict.items():
        heapq.heappush(g_q, (-1 * v, k))
    
    p_dict = defaultdict(list)
    for i in range(len(plays)):
        p_q = p_dict[genres[i]]
        heapq.heappush(p_q, (-1 * plays[i], i))
    
    while len(g_q) > 0:
        p, g = heapq.heappop(g_q)
        p_q = p_dict[g]
        if len(p_q) == 1:
            answer.append(p_q[0][1])
        if len(p_q) > 1:
            answer.append(heapq.heappop(p_q)[1])
            answer.append(heapq.heappop(p_q)[1])
    
    return answer