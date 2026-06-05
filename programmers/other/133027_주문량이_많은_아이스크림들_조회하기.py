# 주문량이 많은 아이스크림들 조회하기
# 프로그래머스 (unknown)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/133027
# 작성자: 지소윤
# 작성일: 2026. 06. 05. 13:45:04

WITH july_summary AS (
    SELECT FLAVOR, SUM(TOTAL_ORDER) AS july_order
    FROM JULY
    GROUP BY FLAVOR
)
SELECT fh.FLAVOR
FROM FIRST_HALF fh
JOIN july_summary j ON fh.FLAVOR = j.FLAVOR
ORDER BY (fh.TOTAL_ORDER + j.july_order) DESC
LIMIT 3;