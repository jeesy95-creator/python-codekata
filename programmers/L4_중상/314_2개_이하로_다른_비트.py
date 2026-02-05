# 2개 이하로 다른 비트
# 프로그래머스 L4 (중상)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/77885
# 알고리즘: 비트연산
# 작성자: 지소윤
# 작성일: 2026. 02. 05. 21:39:51

def solution(numbers):
    answer = []
    
    for x in numbers:
        if x % 2 == 0:
            answer.append(x + 1)
        else:    
            bit = 1
            while x & bit: 
                bit <<= 1

            answer.append(x + bit - (bit >> 1))
    
    return answer


