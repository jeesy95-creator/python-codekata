# 삼총사
# 프로그래머스 L3 (중급)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/131705
# 알고리즘: 완전탐색
# 작성자: 지소윤
# 작성일: 2026. 01. 19. 10:53:43

from itertools import combinations

def solution(number):
    answer = 0
    for combo in combinations(number, 3):
        if sum(combo) == 0:
            answer += 1
    return answer