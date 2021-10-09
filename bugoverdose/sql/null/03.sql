-- NULL 처리하기
-- 생물 종, 이름, 성별 및 중성화 여부를 아이디 순으로 조회하는 SQL문을 작성해주세요. 
-- 이때 이름이 없는 동물의 이름은 "No name"으로 표시해 주세요.

SELECT ANIMAL_TYPE,	IFNULL(NAME, "No name") NAME, SEX_UPON_INTAKE
FROM ANIMAL_INS
ORDER BY ANIMAL_ID;

-- ----------------------------------------------------------------
-- ISNULL(표현식) : 특정 값이 NULL인지 체크하여 NULL이면 1을, 아니면 0을 반환
SELECT ISNULL(NULL); -- 1
SELECT ISNULL(1234); -- 0
-- ----------------------------------------------------------------
-- IFNULL(표현식, NULL일 때의 값) : 기본적으로 인자1을 반환. 다만, 인자1 NULL이면 인자2를 반환.
SELECT IFNULL(NULL, "이 값은 NULL"); -- 이 값은 NULL
SELECT IFNULL(1234, "이 값은 NULL"); -- 1234
-- ----------------------------------------------------------------