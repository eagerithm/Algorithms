-- 없어진 기록 찾기
-- 입양을 간 기록은 있는데, 보호소에 들어온 기록이 없는 동물의 ID와 이름을 ID 순으로 조회하는 SQL문을 작성해주세요.
-- 주의. MySQL에서는 ORACLE의 MINUS 구문 활용 불가

SELECT O.ANIMAL_ID, O.NAME
FROM ANIMAL_INS I RIGHT OUTER JOIN ANIMAL_OUTS O
ON I.ANIMAL_ID = O.ANIMAL_ID
WHERE I.ANIMAL_ID IS NULL 
ORDER BY O.ANIMAL_ID;

-- -------------------------------------------------------------
FROM table1 RIGHT JOIN table2 ON table1.id = table2.id
--   id 값O            id 값O  => INNER JOIN과 동일
--    NULL             id 값O  

-- 주의. MySQL에서는 ORACLE의 FULL OUTER JOIN 사용 불가
SELECT * FROM t1
LEFT JOIN t2 ON t1.id = t2.id
UNION
SELECT * FROM t1
RIGHT JOIN t2 ON t1.id = t2.id
-- -------------------------------------------------------------