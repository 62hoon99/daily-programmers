from collections import deque
def solution(s):
    stack = deque()
    
    for i in range(len(s)):
        if s[i] == "(":
            stack.append(s[i])
        else:
            if len(stack) > 0 and stack[-1] == "(":
                stack.pop()
            else:
                return False
    
    if len(stack) > 0:
        return False
    return True