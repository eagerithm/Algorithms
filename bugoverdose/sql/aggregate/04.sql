-- 중복 제거하기
-- 동물 보호소에 들어온 동물의 이름은 몇 개인지 조회하는 SQL 문을 작성해주세요. 
-- 이때 이름이 NULL인 경우는 집계하지 않으며 중복되는 이름은 하나로 칩니다.

SELECT COUNT(DISTINCT NAME) count -- 96
FROM ANIMAL_INS

-- 96가지 이름 정보, 3개는 중복, 1개는 NULL

-- ----------------------------------------------------------------
-- 중복되는 NAME 값들을 각각 별개로 보는 경우
SELECT COUNT(NAME) count -- 99
FROM ANIMAL_INS

-- ----------------------------------------------------------------
-- 모든 데이터(NULL 포함)
SELECT COUNT(*) count -- 100
FROM ANIMAL_INS

-- ----------------------------------------------------------------
-- NULL일 경우 특정 값으로 대체하면 NULL 자체를 1가지로 계산 가능 
SELECT COUNT(DISTINCT IFNULL(NAME, 1)) -- 97
FROM ANIMAL_INS

SELECT COUNT(IFNULL(NAME, 1)) -- 100
FROM ANIMAL_INS

-- ----------------------------------------------------------------