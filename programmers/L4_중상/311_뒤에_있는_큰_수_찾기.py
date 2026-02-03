# 뒤에 있는 큰 수 찾기
# 프로그래머스 L4 (중상)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/154539
# 알고리즘: 스택
# 작성자: 지소윤
# 작성일: 2026. 02. 03. 15:09:26

def solution(numbers):
    n = len(numbers)
    result = [-1] * n
    st = []  

    for i in range(n):
        while st and numbers[st[-1]] < numbers[i]:
            idx = st.pop()
            result[idx] = numbers[i]
        st.append(i)

    return result 

