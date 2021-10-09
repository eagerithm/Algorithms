-- 동명 동물 수 찾기
-- 동물 보호소에 들어온 동물 이름 중 두 번 이상 쓰인 이름과 해당 이름이 쓰인 횟수를 조회하는 SQL문을 작성해주세요. 
-- 이때 결과는 이름이 없는 동물은 집계에서 제외하며, 결과는 이름 순으로 조회해주세요.

SELECT NAME, COUNT(NAME) count
FROM ANIMAL_INS
GROUP BY NAME
HAVING COUNT(NAME) > 1
ORDER BY NAME

-- ----------------------------------------------------------------
-- The HAVING clause was added to SQL because the WHERE keyword cannot be used with aggregate functions.
-- SELECT column_name(s)          5
-- FROM table_name                1
-- WHERE condition                2
-- GROUP BY column_name(s)        3
-- HAVING condition               4
-- ORDER BY column_name(s);       6
-- ----------------------------------------------------------------