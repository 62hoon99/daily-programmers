def solution(numbers, target):    
    def dfs(depth, num):
        if len(numbers) == depth:
            if num == target:
                return 1
            return 0
        
        return dfs(depth+1, num + numbers[depth]) + dfs(depth+1, num - numbers[depth])
    
    return dfs(0, 0)