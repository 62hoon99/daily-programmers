from collections import defaultdict

def solution(n, results):
    answer = 0
    
    memory_w = defaultdict(set)
    memory_l = defaultdict(set)
    graph_w = defaultdict(list)
    graph_l = defaultdict(list)
    
    for r in results:
        graph_w[r[1]].append(r[0])
        graph_l[r[0]].append(r[1])
    
    def dfs(memory, graph, player):
        if len(memory[player]) > 0:
            return memory[player]
        
        for g in graph[player]:
            for d in dfs(memory, graph, g):
                memory[player].add(d)
    
        memory[player].add(player)
        return memory[player]
    
    for i in range(1, n + 1):
        dfs(memory_w, graph_w, i)
        dfs(memory_l, graph_l, i)
    
    print(memory_l)
    print(memory_w)
    
    for i in range(1, n + 1):
        for m in memory_l[i]:
            memory_w[i].add(m)
    
    for i in range(1, n + 1):
        if len(memory_w[i]) == n:
            answer += 1
    
    return answer