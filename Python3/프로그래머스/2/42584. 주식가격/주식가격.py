from collections import deque

def solution(prices):
    answer = [0] * len(prices)
    stack = deque()
    
    for i in range(len(prices)):
        while len(stack) > 0 and prices[i] < stack[-1][0]:
            price, idx = stack.pop()
            answer[idx] = i - idx
        stack.append((prices[i], i))

    while len(stack) > 0:
        price, idx = stack.pop()
        answer[idx] = len(prices) - 1 - idx
    
    return answer