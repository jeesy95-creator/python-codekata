# 정수 삼각형
# 프로그래머스 (unknown)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/43105
# 작성자: 지소윤
# 작성일: 2026. 05. 26. 10:01:32

def solution(triangle):
    dp = []

    for row in triangle:
        dp.append([0] * len(row))

    dp[0][0] = triangle[0][0]

    for i in range(1, len(triangle)):
        for j in range(len(triangle[i])):

            if j == 0:
                dp[i][j] = dp[i - 1][j] + triangle[i][j]

            elif j == i:
                dp[i][j] = dp[i - 1][j - 1] + triangle[i][j]

            else:
                dp[i][j] = max(dp[i - 1][j - 1], dp[i - 1][j]) + triangle[i][j]

    return max(dp[-1])