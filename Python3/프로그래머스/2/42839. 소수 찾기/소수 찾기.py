def solution(numbers):
    answer = 0
    n_set = set()
    def dfs(n_str, result, k):
        if len(result) == k:
            n_set.add(int(result))
            return
        
        for i in range(len(n_str)):
            left = ""
            right = ""
            if i > 0:
                left = n_str[:i]
            if i < len(n_str) - 1:
                right = n_str[i + 1:]
            dfs(left + right, result + n_str[i], k)
    
    for i in range(len(numbers)):
        dfs(numbers, "", i + 1)
    
    print(n_set)
    
    for n in n_set:
        if n == 0 or n == 1:
            continue
        result = True
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                result = False
                break
        if result:
            answer += 1
    
    return answer