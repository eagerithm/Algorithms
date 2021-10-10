-- 중성화 여부 파악하기 
-- 중성화된 동물은 SEX_UPON_INTAKE 컬럼에 'Neutered' 또는 'Spayed'라는 단어가 들어있습니다. 
-- 동물의 아이디와 이름, 중성화 여부를 아이디 순으로 조회하는 SQL문을 작성해주세요. 
-- 이때 중성화가 되어있다면 'O', 아니라면 'X'라고 표시해주세요.
SELECT ANIMAL_ID, NAME, 
CASE
    WHEN SEX_UPON_INTAKE LIKE "Neutered%" THEN 'O'
    WHEN SEX_UPON_INTAKE LIKE "Spayed%" THEN 'O'
    ELSE 'X'
END AS '중성화'
FROM ANIMAL_INS

-- -----------------------------------------------------
-- 각 데이터에 대해 해당 조건문 실행하여 반환된 값을 SELECT, ORDER BY 등에서 사용
CASE
    WHEN condition1 THEN result1
    WHEN condition2 THEN result2
    WHEN conditionN THEN resultN
    ELSE result
END
-- -----------------------------------------------------
SELECT OrderID, Quantity,
CASE
    WHEN Quantity > 30 THEN 'The quantity is greater than 30'
    WHEN Quantity = 30 THEN 'The quantity is 30'
    ELSE 'The quantity is under 30'
END AS QuantityText
FROM OrderDetails;

SELECT CustomerName, City, Country
FROM Customers
ORDER BY
(CASE
    WHEN City IS NULL THEN Country
    ELSE City
END);
-- -----------------------------------------------------