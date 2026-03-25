def solution(name):
    answer = 0

    for n in name:
        left = ord(n) - ord('A')
        right = 26 - left
        answer += min(left, right)

    # 좌우 이동 최솟값 계산
    n = len(name)
    move = n - 1  # 오른쪽으로만 쭉 가는 기본값

    for i in range(n):
        next_i = i + 1
        # i+1부터 시작하는 연속된 A 구간 건너뛰기
        while next_i < n and name[next_i] == 'A':
            next_i += 1

        # i까지 오른쪽으로 갔다가 되돌아서 왼쪽으로
        go_right_first = i * 2 + (n - next_i)
        # 왼쪽으로 먼저 갔다가 되돌아서 오른쪽으로
        go_left_first = i + (n - next_i) * 2

        move = min(move, go_right_first, go_left_first)

    answer += move

    return answer