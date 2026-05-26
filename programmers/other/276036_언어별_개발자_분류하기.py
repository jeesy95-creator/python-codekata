# 언어별 개발자 분류하기
# 프로그래머스 (unknown)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/276036
# 작성자: 지소윤
# 작성일: 2026. 05. 26. 12:42:04

SELECT
    CASE
        WHEN
            SKILL_CODE & (
                SELECT SUM(CODE)
                FROM SKILLCODES
                WHERE CATEGORY = 'Front End'
            )
            AND
            SKILL_CODE & (
                SELECT CODE
                FROM SKILLCODES
                WHERE NAME = 'Python'
            )
        THEN 'A'

        WHEN
            SKILL_CODE & (
                SELECT CODE
                FROM SKILLCODES
                WHERE NAME = 'C#'
            )
        THEN 'B'

        WHEN
            SKILL_CODE & (
                SELECT SUM(CODE)
                FROM SKILLCODES
                WHERE CATEGORY = 'Front End'
            )
        THEN 'C'
    END AS GRADE,
    ID,
    EMAIL
FROM DEVELOPERS
HAVING GRADE IS NOT NULL
ORDER BY GRADE, ID;