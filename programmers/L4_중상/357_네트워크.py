# 네트워크
# 프로그래머스 L4 (중상)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/43162
# 알고리즘: DFS/BFS
# 작성자: 지소윤
# 작성일: 2026. 02. 12. 09:45:26

def solution(n, computers):
    visited = [False] * n
    
    def dfs(v):
        visited[v] = True
        for nxt in range(n):
            if computers[v][nxt] == 1 and not visited[nxt]:
                dfs(nxt)
    count = 0
    for i in range(n):
        if not visited[i]:
            count += 1
            dfs(i)
    return count 
                
        