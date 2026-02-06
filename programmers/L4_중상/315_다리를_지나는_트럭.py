# 다리를 지나는 트럭
# 프로그래머스 L4 (중상)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/42583
# 알고리즘: 스택/큐, 시뮬레이션
# 작성자: 지소윤
# 작성일: 2026. 02. 06. 15:00:31

from collections import deque

def solution(bridge_length, weight, truck_weights):
    time = 0
    bridge = deque([0] * bridge_length)
    trucks = deque(truck_weights)
    bridge_weight = 0
    
    while trucks or bridge_weight > 0:
        time += 1
        
        out = bridge.popleft()
        bridge_weight -= out
        
        if trucks:
            if bridge_weight + trucks[0] <= weight:
                truck = trucks.popleft()
                bridge.append(truck)
                bridge_weight += truck
            else:
                bridge.append(0)
    
    return time

