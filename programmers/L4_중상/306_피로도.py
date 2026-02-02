# 피로도
# 프로그래머스 L4 (중상)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/87946
# 알고리즘: 완전탐색, 백트래킹
# 작성자: 지소윤
# 작성일: 2026. 02. 02. 13:43:51

from itertools import permutations

def solution(k, dungeons):
    answer = 0

    for order in permutations(dungeons):
        cur = k
        cnt = 0

        for need, cost in order:
            if cur >= need:
                cur -= cost
                cnt += 1
            else:
                break

        answer = max(answer, cnt)

    return answer


    
    
    