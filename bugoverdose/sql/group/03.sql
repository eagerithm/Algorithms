-- 입양 시각 구하기(1)
-- 09:00부터 19:59까지, 각 시간대별로 입양이 몇 건이나 발생했는지 조회하는 SQL문을 작성 
-- 결과는 시간대 순으로 정렬

SELECT HOUR(DATETIME) HOUR, COUNT(*) COUNT
FROM ANIMAL_OUTS
GROUP BY HOUR(DATETIME) -- 해당 함수 실행결과가 동일한 데이터만 같은 그룹으로
HAVING HOUR >= 9 and HOUR <= 19 -- 에러: HAVING HOUR(DATETIME) >= 9 and HOUR(DATETIME) <= 20
ORDER BY HOUR

-- SELECT HOUR(DATETIME) as 'HOUR', COUNT(*) as 'COUNT'
-- FROM ANIMAL_OUTS
-- GROUP BY HOUR(DATETIME)
-- HAVING HOUR >= 9 and HOUR <= 19
-- ORDER BY HOUR(DATETIME) ASC
-- ----------------------------------------------------------------
-- ----------------------------------------------------------------