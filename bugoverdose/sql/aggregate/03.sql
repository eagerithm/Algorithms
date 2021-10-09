-- 동물 수 구하기
-- 동물 보호소에 동물이 몇 마리 들어왔는지 조회하는 SQL 문을 작성해주세요.

SELECT COUNT(*) count -- 특정 조건에 부합하는 데이터의 개수를 출력(조건이 없으면 전체 데이터 수)
FROM ANIMAL_INS

SELECT SUM(1) count -- 전체 데이터 수만큼 1이라는 값들의 합을 count 컬럼에 출력 (100개 데이터 => count 100)
FROM ANIMAL_INS

-- ----------------------------------------------------------------
SELECT SUM(3) count -- 전체 데이터 수*3만큼 count 컬럼에 출력 (100개 데이터 => count 300)
FROM ANIMAL_INS

-- ----------------------------------------------------------------
-- SUM() Syntax: The SUM() function returns the total sum of a numeric column.
SELECT SUM(column_name)
FROM table_name
WHERE condition -- 조건이 없으면 모든 데이터에 대해 합침

-- ----------------------------------------------------------------
-- COUNT() Syntax: The COUNT() function returns the number of rows that matches a specified criterion.
SELECT COUNT(column_name)
FROM table_name
WHERE condition

-- ----------------------------------------------------------------