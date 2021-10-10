-- 오랜 기간 보호한 동물(2)
-- 입양을 간 동물 중, 보호 기간이 가장 길었던 동물 두 마리의 아이디와 이름을 조회하는 SQL문을 작성해주세요. 
-- 이때 결과는 보호 기간이 긴 순으로 조회해야 합니다.
-- 테이블 2개에서 서로 대응되는 데이터의 컬럼 값 비교
SELECT O.ANIMAL_ID, O.NAME
FROM ANIMAL_INS I INNER JOIN ANIMAL_OUTS O 
ON I.ANIMAL_ID = O.ANIMAL_ID
ORDER BY O.DATETIME - I.DATETIME DESC
LIMIT 2

-- -----------------------------------------------------