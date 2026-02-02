# 타겟 넘버
# 프로그래머스 L4 (중상)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/43165
# 알고리즘: DFS, 완전탐색
# 작성자: 지소윤
# 작성일: 2026. 02. 03. 00:03:10

from collections import deque

def solution(numbers, target):
    n = len(numbers)
    q = deque()
    
    q.append((0, 0))
    
    count = 0
    
    while q:
        idx, cur_sum = q.popleft()        
        if idx == n:
            if cur_sum == target:
                count +=1
                  
        else:
            x = numbers[idx]
            q.append((idx+1, cur_sum + x))
            q.append((idx+1, cur_sum - x))

               
    return count
