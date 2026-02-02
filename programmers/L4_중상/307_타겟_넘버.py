# 타겟 넘버
# 프로그래머스 L4 (중상)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/43165
# 알고리즘: DFS, 완전탐색
# 작성자: 지소윤
# 작성일: 2026. 02. 02. 23:35:48

def solution(numbers, target):
    n = len(numbers)

    def dfs(idx, cur_sum):
        if idx == n:
            if cur_sum == target:
                return 1
            else:
                return 0
            
        plus_case = dfs(idx + 1, cur_sum + numbers[idx])
        minus_case = dfs(idx + 1, cur_sum - numbers[idx])

        return plus_case + minus_case
        
    return dfs(0, 0)

    
    