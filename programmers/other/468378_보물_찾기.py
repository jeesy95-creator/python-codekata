# 보물 찾기
# 프로그래머스 (unknown)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/468378
# 작성자: 지소윤
# 작성일: 2026. 05. 21. 18:56:11

def solution(depth, money, excavate):
    w = len(depth)

    # 1번 열 기준으로 사용
    cost = [[0] * (w + 2) for _ in range(w + 2)]
    pick = [[0] * (w + 2) for _ in range(w + 2)]

    # 1단계: 각 구간의 최소 최악 비용과 첫 굴착 위치 계산
    for length in range(1, w + 1):
        for L in range(1, w - length + 2):
            R = L + length - 1

            best_cost = float('inf')

            for k in range(L, R + 1):
                left_cost = cost[L][k - 1]
                right_cost = cost[k + 1][R]

                candidate = depth[k - 1] + max(left_cost, right_cost)

                if candidate < best_cost:
                    best_cost = candidate
                    cost[L][R] = candidate
                    pick[L][R] = k

    # 2단계: 계산한 전략표를 따라 실제 굴착
    L, R = 1, w

    while L <= R:
        k = pick[L][R]
        result = excavate(k)

        if result == 0:
            return k
        elif result == -1:
            R = k - 1
        else:  # result == 1
            L = k + 1