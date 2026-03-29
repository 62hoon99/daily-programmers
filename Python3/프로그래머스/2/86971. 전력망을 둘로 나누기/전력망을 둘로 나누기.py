from collections import defaultdict, deque

def solution(n, wires):
    answer = 100
    
    d_wires = defaultdict(list)
    for w in wires:
        d_wires[w[0]].append(w)
        d_wires[w[1]].append(w)
    
    def bfs(ext):
        q = deque()
        
        for w in wires:
            if not (ext[0] == w[0] and ext[1] == w[1]):
                q.append(w[0])
                break
        
        memory = set()
        
        while len(q) > 0:
            current = q.popleft()
            memory.add(current)
            for elem in d_wires[current]:
                if not (ext[0] == elem[0] and ext[1] == elem[1]):
                    c = elem[0]
                    if current == elem[0]:
                        c = elem[1]
                    if c not in memory:
                        q.append(c)
        
        return len(memory)
    
    for w in wires:
        result = abs(n - bfs(w))
        opo = n - result
        
        answer = min(answer, abs(result - opo))
    
    return answer