-- 이름에 el이 들어가는 동물 찾기
-- 이름에 "EL"이 들어가는 개의 아이디와 이름을 조회하는 SQL문을 작성해주세요. 이때 결과는 이름 순으로 조회해주세요. 
-- 단, 이름의 대소문자는 구분하지 않습니다.
SELECT ANIMAL_ID, NAME
FROM ANIMAL_INS
WHERE NAME LIKE '%el%' and ANIMAL_TYPE = "Dog"
ORDER BY NAME;

-- -----------------------------------------------------
-- 기본적으로 전부 case insensitive
WHERE NAME LIKE '%el%' -- Elijah, Shelly 등 el이 어디든지 포함된 NAME 값
WHERE NAME LIKE '%el' -- el로 끝나는 NAME 값
WHERE NAME LIKE 'el%' -- Elijah 등 el로 시작되는 NAME 값

WHERE NAME LIKE '% el %' -- " el "이 포함된 값, 즉 공백도 포함
-- -----------------------------------------------------
-- LIKE Syntax
SELECT column1, column2, ...
FROM table_name
WHERE columnN LIKE pattern;

-- There are two wildcards often used in conjunction with the LIKE operator:
The percent sign (%) represents zero, one, or multiple characters -- %: 해당 방향은 자유 형식
The underscore sign (_) represents one, single character -- _ : 아무거나 한글자 필요
-- -----------------------------------------------------
LIKE 'a%'	Finds any values that start with "a"
LIKE '%a'	Finds any values that end with "a"
LIKE '%or%'	Finds any values that have "or" in any position
LIKE 'a%o'	Finds any values that start with "a" and ends with "o" -- a~~~o

LIKE '_r%'	Finds any values that have "r" in the second position -- ~r~~~~~
LIKE 'a_%'	Finds any values that start with "a" and are at least 2 characters in length
LIKE 'a__%'	Finds any values that start with "a" and are at least 3 characters in length
-- -----------------------------------------------------
