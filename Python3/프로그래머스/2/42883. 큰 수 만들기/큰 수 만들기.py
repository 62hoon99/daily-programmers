def solution(number, k):
    answer = ''
    stack = []
    count = 0
    
    for n in number:
        s = int(n)
        while count < k and len(stack) > 0 and stack[-1] < s:
            count += 1
            stack.pop()
        stack.append(s)
    
    if len(stack) > (len(number) - k):
        stack.pop()
    
    for s in stack:
        answer += str(s)
    
    return answer