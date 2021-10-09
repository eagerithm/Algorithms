-- 이름이 있는 동물의 아이디
-- 이름이 있는 동물의 ID를 조회하는 SQL 문을 작성해주세요. 단, ID는 오름차순 정렬되어야 합니다.

SELECT ANIMAL_ID
FROM ANIMAL_INS
WHERE NAME is not NULL
ORDER BY ANIMAL_ID;

-- ----------------------------------------------------------------