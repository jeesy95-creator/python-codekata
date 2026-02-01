# 괄호 회전하기
# 프로그래머스 L4 (중상)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/76502
# 알고리즘: 스택, 문자열
# 작성자: 지소윤
# 작성일: 2026. 02. 02. 04:34:07

def solution(s):
    n = len(s)
    if n % 2 == 1:
        return 0

    pair = {')': '(', ']': '[', '}': '{'}
    opens = set(pair.values())

    def is_valid(t: str) -> bool:
        stack = []
        for ch in t:
            if ch in opens:
                stack.append(ch)
            else:
                if not stack or stack[-1] != pair[ch]:
                    return False
                stack.pop()
        return not stack

    answer = 0
    for i in range(n):
        rotated = s[i:] + s[:i]
        if is_valid(rotated):
            answer += 1

    return answer

                
       



