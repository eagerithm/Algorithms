-- 입양 시각 구하기(2)
-- 0시부터 23시까지, 각 시간대별로 입양이 몇 건이나 발생했는지 조회하는 SQL문을 작성
-- 이때 결과는 시간대 순으로 정렬
-- 핵심 : 0시~6시 등 해당되는 데이터가 전혀 없는 그룹도 명시해야 함 => 변수 선언 필요

SET @hour := -1; -- ; 필수

SELECT (@hour := @hour + 1) as HOUR -- @hour의 값을 1씩 증가시키면서 SELECT문 전체를 반복 실행
, (
    SELECT COUNT(*) 
    FROM ANIMAL_OUTS
    WHERE HOUR(DATETIME) = @hour
  ) as COUNT
FROM ANIMAL_OUTS
WHERE @hour < 23;

-- ----------------------------------------------------------------
-- 재귀쿼리와 left join 활용하는 방법
WITH RECURSIVE HOUR AS(
SELECT 0 AS h -- (3)
UNION ALL -- (2)
SELECT h+1 FROM HOUR WHERE h<23); -- (4), (5)

SELECT h AS HOUR, COALESCE(COUNT(ANIMAL_ID),0) AS COUNT
FROM HOUR LEFT JOIN ANIMAL_OUTS ANI ON HOUR.h = HOUR(ANI.DATETIME)
GROUP BY HOUR.h;

-- WITH RECURSIVE 정리
-- (1) 메모리 상에 가상의 테이블을 저장
-- (2) 반드시 UNION 사용
-- (3) 반드시 비반복문도 최소한 1개 요구됨
-- (4) 서브쿼리에서 바깥의 가상의 테이블을 참조하는 문장(반복문)이 반드시 필요함
-- (5) 반복되는 문장은 반드시 정지조건이 요구됨
-- (6) 가상의 테이블을 구성하면서 자신을 참조하여 값을 결정할 때 유용함

-- ----------------------------------------------------------------