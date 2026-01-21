from collections import deque
def solution(progresses, speeds):
    l = list()
    
    for i in range(len(progresses)):
        n = (100 - progresses[i]) // speeds[i]
        m = (100 - progresses[i]) % speeds[i]
        if m > 0:
            n += 1
        l.append(n)

    result = []
    
    num = l[0]
    sum = 1
    for i in range(1, len(l)):
        if num >= l[i]:
            sum += 1
        else:
            result.append(sum)
            num = l[i]
            sum = 1
    
    result.append(sum)
        
    return result