# 소수 찾기
# 프로그래머스 L4 (중상)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/42839
# 알고리즘: 완전탐색, 수학
# 작성자: 지소윤
# 작성일: 2026. 02. 20. 09:49:22

from itertools import permutations

def solution(numbers):
    result_set = set()
    
    
    for i in range(1, len(numbers) + 1):
        for combo in permutations(numbers, i):
            num_str = ''.join(combo)
            result_set.add(int(num_str))
    
    
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True
    
    
    count = 0
    for num in result_set:
        if is_prime(num):
            count += 1
    
    return count