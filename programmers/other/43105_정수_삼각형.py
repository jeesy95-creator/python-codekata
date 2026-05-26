# 정수 삼각형
# 프로그래머스 (unknown)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/43105
# 작성자: 지소윤
# 작성일: 2026. 05. 26. 10:03:01

def solution(triangle):
    dp = triangle[-1][:]

    for i in range(len(triangle) - 2, -1, -1):
        for j in range(len(triangle[i])):
            dp[j] = triangle[i][j] + max(dp[j], dp[j + 1])

    return dp[0]