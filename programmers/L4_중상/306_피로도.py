# 피로도
# 프로그래머스 L4 (중상)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/87946
# 알고리즘: 완전탐색, 백트래킹
# 작성자: 지소윤
# 작성일: 2026. 02. 02. 13:44:13

def solution(k, dungeons):
    n = len(dungeons)
    best = 0

    def dfs(cur, mask, cnt):
        nonlocal best
        best = max(best, cnt)

        for i in range(n):
            if mask & (1 << i):
                continue

            need, cost = dungeons[i]
            if cur >= need:
                dfs(cur - cost, mask | (1 << i), cnt + 1)

    dfs(k, 0, 0)
    return best

    return answer


    
    
    