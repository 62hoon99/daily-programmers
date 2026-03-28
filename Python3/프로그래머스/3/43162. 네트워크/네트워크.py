def solution(n, computers):
    answer = 0
    
    memory = set()
    
    def dfs(idx):
        for i in range(len(computers[idx])):
            if i == idx:
                continue
            c = computers[idx][i]
            if c == 1 and i not in memory:
                memory.add(i)
                dfs(i)
    
    for i in range(len(computers)):
        if i not in memory:
            memory.add(i)
            dfs(i)
            answer += 1
    
    return answer