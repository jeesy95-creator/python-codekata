# 최소직사각형
# 프로그래머스 L3 (중급)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/86491
# 알고리즘: 완전탐색, 그리디
# 작성자: 지소윤
# 작성일: 2026. 01. 30. 10:21:01

def solution(sizes):
    for card in sizes:
        if card[0] < card[1]:
            card[0], card[1] = card[1], card[0]
    
    max_width = max(card[0] for card in sizes)   
    max_height = max(card[1] for card in sizes)  
    
    
    return max_width * max_height