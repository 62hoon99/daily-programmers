from collections import deque

def solution(bridge_length, weight, truck_weights):
    bridge = deque() # 다리
    count = 0 # 통과한 트럭 개수
    total_weight = 0 # 총 무개
    
    timer = 0 # 타이머
    idx = 0 # 다음으로 올라타야 하는 truck index
    
    while count < len(truck_weights):
        timer += 1
        
        # 다리 통과 처리
        if len(bridge) == bridge_length:
            truck_weight = bridge.popleft()
            if truck_weight > 0:
                total_weight -= truck_weight
                count += 1
        
        # 다리 위로 올라타는 처리
        if idx < len(truck_weights) and total_weight + truck_weights[idx] <= weight:
            bridge.append(truck_weights[idx])
            total_weight += truck_weights[idx]
            idx += 1
        else:
            bridge.append(0)
    
    return timer
            