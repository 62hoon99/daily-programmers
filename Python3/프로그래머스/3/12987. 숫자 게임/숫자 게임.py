from bisect import bisect_right, insort

def solution(A, B):
    answer = 0
    b_sorted = sorted(B)  # 중복 포함 정렬 리스트

    for a in A:
        # a보다 큰 값 중 가장 작은 것의 index 탐색
        idx = bisect_right(b_sorted, a)

        if idx < len(b_sorted):
            # 이길 수 있는 카드가 있으면 사용
            answer += 1
            del b_sorted[idx]
        else:
            # 이길 수 없으면 가장 작은 카드를 희생
            del b_sorted[0]

    return answer