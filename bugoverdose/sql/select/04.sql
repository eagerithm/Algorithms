-- 어린 동물 찾기
-- 젊은(=Aged가 아닌) 동물의 아이디와 이름을 조회하는 SQL 문을 작성해주세요
SELECT ANIMAL_ID, NAME
FROM ANIMAL_INS
WHERE INTAKE_CONDITION != "Aged"
ORDER BY ANIMAL_ID

-- ----------------------------------------------------------------