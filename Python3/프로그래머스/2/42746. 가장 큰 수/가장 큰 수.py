import heapq
def solution(numbers):
    answer = ''
    
    str_max_num = str(max(numbers))
    max_len = len(str_max_num)
    heap = []
    for n in numbers:
        str_n = str(n)
        str_n = (str_n * (max_len + 1))[:max_len + 1]
        heapq.heappush(heap, (-1 * int(str_n), n))
    
    while len(heap) > 0:
        element = heapq.heappop(heap)
        answer = answer + str(element[1])
    
    if answer[0] == "0":
        return "0"
    return answer