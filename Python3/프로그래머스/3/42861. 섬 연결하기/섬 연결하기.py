import heapq
from collections import defaultdict

def solution(n, costs):
    # 1. 인접 리스트 형태로 그래프 구성
    #    graph[노드] = [(비용, 연결된 노드), ...]
    graph = defaultdict(list)
    for a, b, weight in costs:
        graph[a].append((weight, b))
        graph[b].append((weight, a))  # 양방향

    # 2. 시작 노드 0번을 MST에 포함
    visited = set()
    visited.add(0)

    # 3. 시작 노드에서 뻗어나갈 수 있는 간선들을 힙에 추가
    #    힙 구조: (비용, 목적지 노드)
    #    heapq는 튜플의 첫 번째 원소 기준으로 최솟값을 꺼내므로 비용을 앞에 둠
    min_heap = []
    for weight, next_node in graph[0]:
        heapq.heappush(min_heap, (weight, next_node))

    answer = 0

    # 4. 힙이 빌 때까지 반복
    while min_heap:
        # 4-1. 현재 MST에서 뻗을 수 있는 간선 중 비용이 가장 작은 것을 꺼냄
        weight, node = heapq.heappop(min_heap)

        # 4-2. 이미 MST에 포함된 노드면 스킵 (이 간선을 쓰면 사이클 발생)
        if node in visited:
            continue

        # 4-3. MST에 해당 노드 추가, 비용 누적
        visited.add(node)
        answer += weight

        # 4-4. 새로 추가된 노드에서 뻗어나갈 수 있는 간선들을 힙에 추가
        #       단, 이미 MST에 포함된 노드로 가는 간선은 추가해도 4-2에서 걸러짐
        for next_weight, next_node in graph[node]:
            if next_node not in visited:
                heapq.heappush(min_heap, (next_weight, next_node))

    return answer