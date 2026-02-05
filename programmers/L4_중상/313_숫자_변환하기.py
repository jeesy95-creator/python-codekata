# 숫자 변환하기
# 프로그래머스 L4 (중상)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/154538
# 알고리즘: BFS, DP
# 작성자: 지소윤
# 작성일: 2026. 02. 05. 20:02:39

from collections import deque

def solution(x, y, n):
    if x == y:
        return 0
    
    queue = deque([(x, 0)])
    visited = set([x])
    
    while queue:
        current, count = queue.popleft()
        
        next_values = [
            current + n,
            current * 2,
            current * 3
        ]
        
        for next_val in next_values:
            if next_val == y:
                return count + 1
            elif next_val < y and next_val not in visited:
                queue.append((next_val, count + 1))
                visited.add(next_val)
            
                 
    return -1
    
   