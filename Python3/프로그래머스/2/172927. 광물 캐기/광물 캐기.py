from collections import deque

def solution(picks, minerals):
    answer = 0
    
    # 1. mineral 최대 캘 수 있는 갯수 세기
    total_picks = sum(picks)
    avail_mine = total_picks * 5
    minerals = minerals[:avail_mine]
    
    # 2. 각 곡갱이 별로 5범위로 피로도 계산
    dia_tl = []
    iron_tl = []
    stone_tl = []
    
    dia_sum = 0
    iron_sum = 0
    stone_sum = 0
    
    for i in range(len(minerals)):
        dia_sum += 1
        
        m = minerals[i]
        
        if m == 'diamond':
            iron_sum += 5
            stone_sum += 25
        elif m == 'iron':
            iron_sum += 1
            stone_sum += 5
        else:
            iron_sum += 1
            stone_sum += 1
        
        if i % 5 == 4:
            dia_tl.append(dia_sum)
            iron_tl.append(iron_sum)
            stone_tl.append(stone_sum)
            dia_sum = 0
            iron_sum = 0
            stone_sum = 0
    
    if dia_sum > 0:
        dia_tl.append(dia_sum)
        iron_tl.append(iron_sum)
        stone_tl.append(stone_sum)
    
    # 3. 돌 기준으로 5범위의 피로도 계산
    tired_list = []
    for i in range(len(stone_tl)):
        tired_list.append((stone_tl[i], i))
    
    # 4. (3)에서 구한 값 정렬
    tired_list.sort(reverse = True)
    
    # 5. 최솟 값의 범위에 해당하는 값을 각 곡갱이의 피로도에서 가져와서 더하기
    p_q = deque()
    for i in range(len(picks)):
        for _ in range(picks[i]):
            if i == 0:
                p_q.append('dia')
            elif i == 1:
                p_q.append('iron')
            else:
                p_q.append('stone')
    
    for tired in tired_list:
        t = tired[0]
        idx = tired[1]
        
        p = p_q.popleft()
        
        if p == 'dia':
            answer += dia_tl[idx]
        elif p == 'iron':
            answer += iron_tl[idx]
        else:
            answer += stone_tl[idx]
    
    return answer