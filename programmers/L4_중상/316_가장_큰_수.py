# 가장 큰 수
# 프로그래머스 L4 (중상)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/42746
# 알고리즘: 정렬
# 작성자: 지소윤
# 작성일: 2026. 02. 09. 15:49:31

from functools import cmp_to_key

def solution(numbers):
    numbers = [str(num) for num in numbers]
    
    def compare(a, b):
        if a + b > b + a:
            return -1  
        elif a + b < b + a:
            return 1   
        else:
            return 0   
    
    numbers = sorted(numbers, key=cmp_to_key(compare))    
    answer = ''.join(numbers)
    

    if answer[0] == '0':
        return '0'
    
    return answer