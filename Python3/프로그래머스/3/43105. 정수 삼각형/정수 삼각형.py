def solution(triangle):
    memory = []
    
    for i in range(1, len(triangle) + 1):
        memory.append([-1] * i)
    
    memory[0][0] = triangle[0][0]
    
    for i in range(len(triangle) - 1):
        t_l = triangle[i]
        
        for j in range(len(t_l)):
            memory[i+1][j] = max(memory[i][j] + triangle[i+1][j], memory[i+1][j])
            memory[i+1][j+1] = max(memory[i][j] + triangle[i+1][j+1], memory[i+1][j+1])
    
    return max(memory[-1])