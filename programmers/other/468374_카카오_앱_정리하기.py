# 카카오 앱 정리하기
# 프로그래머스 (unknown)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/468374
# 작성자: 지소윤
# 작성일: 2026. 05. 23. 21:36:28

from collections import deque


def solution(board, commands):
    H = len(board)
    W = len(board[0])

    # 1: 오른쪽, 2: 아래, 3: 왼쪽, 4: 위
    dirs = [
        (1, 0),
        (0, 1),
        (-1, 0),
        (0, -1)
    ]

    def parse_apps():
        apps = {}

        for y in range(H):
            for x in range(W):
                app_id = board[y][x]

                if app_id == 0 or app_id in apps:
                    continue

                size = 1
                while y + size < H and board[y + size][x] == app_id:
                    size += 1

                # [왼쪽 x, 위쪽 y, size - 1]
                apps[app_id] = [x, y, size - 1]

        return apps

    def is_overlap(a, b):
        ax1, ay1 = a[0], a[1]
        ax2, ay2 = a[0] + a[2], a[1] + a[2]

        bx1, by1 = b[0], b[1]
        bx2, by2 = b[0] + b[2], b[1] + b[2]

        return not (
            ax2 < bx1 or
            ax1 > bx2 or
            ay2 < by1 or
            ay1 > by2
        )

    def is_overflow(app):
        x, y, size = app

        if x < 0 or x + size >= W:
            return True

        if y < 0 or y + size >= H:
            return True

        return False

    def move_app(app_id, arrow, count, to_move):
        app = apps[app_id]
        dx, dy = dirs[arrow - 1]

        for _ in range(count):
            app[0] += dx
            app[1] += dy

            if count == 1 and is_overflow(app):
                to_move.append(app_id)
                break

            for other_id in apps:
                if other_id == app_id or other_id in to_move:
                    continue

                if is_overlap(app, apps[other_id]):
                    move_app(other_id, arrow, 1, to_move)

    apps = parse_apps()

    for app_id, arrow in commands:
        to_move = deque()

        move_app(app_id, arrow, 1, to_move)

        while to_move:
            cur_id = to_move[0]
            cur_app = apps[cur_id]
            size = cur_app[2]

            if arrow == 1:
                cur_app[0] = -1 - size
            elif arrow == 2:
                cur_app[1] = -1 - size
            elif arrow == 3:
                cur_app[0] = W
            else:
                cur_app[1] = H

            move_app(cur_id, arrow, size + 1, to_move)
            to_move.popleft()

    answer = [[0] * W for _ in range(H)]

    for app_id, app in apps.items():
        x, y, size = app

        for r in range(y, y + size + 1):
            for c in range(x, x + size + 1):
                answer[r][c] = app_id

    return answer