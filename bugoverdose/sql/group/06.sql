-- https://www.notion.so/workgony/DB-2-SQL-7f13d4f7e3494c75ae128c1573741b25

-- Q1. Q-init 의 쿼리를 수행한 후, languages 테이블에서 language_id가 중복된 경우에 대해 language_id, count 를 출력하시오
SELECT language_id, COUNT(*)
FROM languages
GROUP BY language_id
HAVING COUNT(*) > 1;

-- Q2. languages 테이블에 대해 language_id 별로 순위를 매겨보세요
SELECT language_id
, language_name
, created_at
, row_number() over (partition by language_id) as rnum
FROM languages;

-- Q3. 중복된 language_id를 가진 대상 중에서 delete 할 대상(나중에 입력된)만 출력하시오
SELECT A.language_id
, A.language_name
, A.created_at
FROM (
  SELECT language_id
  , language_name
  , created_at
  , row_number() over (partition by language_id ORDER BY created_at) as rnum
  FROM languages
) A
WHERE A.rnum > 1;

-- Q4. Q3을 이용하여 중복 날리기
-- *hint: select ctid from languages 는 unique 한 key값을 출력해준다
DELETE FROM languages
WHERE ctid IN (
  SELECT A.ctid
  FROM (
    SELECT ctid    
    , row_number() over (partition by language_id ORDER BY created_at) as rnum
    FROM languages
  ) A
  WHERE A.rnum > 1
);

-- ----------------------------------------------------------------