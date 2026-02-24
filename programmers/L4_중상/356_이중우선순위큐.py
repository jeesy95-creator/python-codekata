# 이중우선순위큐
# 프로그래머스 L4 (중상)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/42628
# 알고리즘: 힙
# 작성자: 지소윤
# 작성일: 2026. 02. 24. 09:39:24

def solution(operations):
    queue = []
    for op in operations:
        cmd, num = op.split()
        num = int(num)
        if cmd == "I":
            queue.append(num)
        else:
            if not queue:
                pass
            elif num == 1:
                queue.remove(max(queue))
            else:
                queue.remove(min(queue))
    
    if not queue:
        return [0, 0]
    else:
        return [max(queue), min(queue)]