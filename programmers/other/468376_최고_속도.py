# 최고 속도
# 프로그래머스 (unknown)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/468376
# 작성자: 지소윤
# 작성일: 2026. 05. 22. 17:32:13

import heapq


def solution(city, road):
    # 1. 도로 정보 정리
    roads = []

    for road_info in road:
        x1, y1, x2, y2, limit = road_info

        start_point = (x1, y1)
        end_point = (x2, y2)

        if y1 == y2:
            # 가로 도로
            roads.append({
                "direction": "horizontal",
                "start": start_point,
                "end": end_point,
                "x_range": (x1, x2),
                "fixed_y": y1,
                "camera": ((x1 + x2) // 2, y1),
                "limit": limit
            })

        else:
            # 세로 도로
            roads.append({
                "direction": "vertical",
                "start": start_point,
                "end": end_point,
                "y_range": (y1, y2),
                "fixed_x": x1,
                "camera": (x1, (y1 + y2) // 2),
                "limit": limit
            })

    # 2. 각 도로 위의 중요한 점 모으기
    points_on_road = [set() for _ in roads]

    for i, r in enumerate(roads):
        points_on_road[i].add(r["start"])
        points_on_road[i].add(r["end"])
        points_on_road[i].add(r["camera"])

    # 3. 도시 좌표를 도시가 놓인 도로에 추가
    for city_position in city:
        cx, cy = city_position

        for i, r in enumerate(roads):
            if r["direction"] == "horizontal":
                x1, x2 = r["x_range"]

                if cy == r["fixed_y"] and x1 <= cx <= x2:
                    points_on_road[i].add((cx, cy))

            else:
                y1, y2 = r["y_range"]

                if cx == r["fixed_x"] and y1 <= cy <= y2:
                    points_on_road[i].add((cx, cy))

    # 4. 두 도로의 교차점 찾기
    def intersection(r1, r2):
        # 가로 + 세로
        if r1["direction"] == "horizontal" and r2["direction"] == "vertical":
            px = r2["fixed_x"]
            py = r1["fixed_y"]

            hx1, hx2 = r1["x_range"]
            vy1, vy2 = r2["y_range"]

            if hx1 <= px <= hx2 and vy1 <= py <= vy2:
                return (px, py)

            return None

        # 세로 + 가로
        if r1["direction"] == "vertical" and r2["direction"] == "horizontal":
            px = r1["fixed_x"]
            py = r2["fixed_y"]

            vy1, vy2 = r1["y_range"]
            hx1, hx2 = r2["x_range"]

            if hx1 <= px <= hx2 and vy1 <= py <= vy2:
                return (px, py)

            return None

        # 세로 + 세로
        if r1["direction"] == "vertical" and r2["direction"] == "vertical":
            if r1["fixed_x"] != r2["fixed_x"]:
                return None

        # 가로 + 가로
        if r1["direction"] == "horizontal" and r2["direction"] == "horizontal":
            if r1["fixed_y"] != r2["fixed_y"]:
                return None

        # 같은 직선 위의 도로는 문제 조건상
        # 만난다면 끝점 하나만 공유
        common_endpoints = {
            r1["start"],
            r1["end"]
        } & {
            r2["start"],
            r2["end"]
        }

        if common_endpoints:
            return common_endpoints.pop()

        return None

    # 5. 교차점을 각 도로의 점 목록에 추가
    for i in range(len(roads)):
        for j in range(i + 1, len(roads)):
            cross_point = intersection(roads[i], roads[j])

            if cross_point is not None:
                points_on_road[i].add(cross_point)
                points_on_road[j].add(cross_point)

    # 6. 좌표 -> 그래프 정점 id
    point_id = {}
    graph = []

    def get_id(point):
        if point not in point_id:
            point_id[point] = len(point_id)
            graph.append([])

        return point_id[point]

    # 7. 각 도로 위 점들을 정렬하고 이웃한 점끼리 연결
    for i, r in enumerate(roads):
        points = points_on_road[i]

        if r["direction"] == "horizontal":
            points = sorted(points, key=lambda p: p[0])
        else:
            points = sorted(points, key=lambda p: p[1])

        for idx in range(len(points) - 1):
            p1 = points[idx]
            p2 = points[idx + 1]

            u = get_id(p1)
            v = get_id(p2)

            graph[u].append(v)
            graph[v].append(u)

    # 8. 카메라 정점의 제한속도 기록
    camera_limit = {}

    for r in roads:
        camera_id = get_id(r["camera"])
        limit = r["limit"]

        if camera_id not in camera_limit:
            camera_limit[camera_id] = limit
        else:
            camera_limit[camera_id] = min(camera_limit[camera_id], limit)

    # 9. 도시 좌표 -> 그래프 정점 id
    city_id = []

    for city_position in city:
        city_id.append(get_id(tuple(city_position)))

    # 10. 최대 병목 경로
    # best[v] = 1번 도시에서 v까지 갈 때 가능한 최고 속도
    INF = float("inf")

    best = [-1] * len(graph)
    start = city_id[0]
    best[start] = INF

    heap = [(-INF, start)]

    while heap:
        neg_speed, cur = heapq.heappop(heap)
        speed = -neg_speed

        if speed < best[cur]:
            continue

        for nxt in graph[cur]:
            next_speed = speed

            # 다음 정점이 카메라 위치면 제한 반영
            if nxt in camera_limit:
                next_speed = min(next_speed, camera_limit[nxt])

            if next_speed > best[nxt]:
                best[nxt] = next_speed
                heapq.heappush(heap, (-next_speed, nxt))

    # 11. 답 만들기
    answer = []

    for target in city_id[1:]:
        if best[target] == INF:
            # 카메라를 하나도 지나지 않고 도달 가능
            answer.append(0)
        else:
            answer.append(best[target])

    return answer