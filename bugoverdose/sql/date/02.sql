-- DATETIME에서 DATE로 형 변환
-- 각 동물의 아이디와 이름, 들어온 날짜1를 조회하는 SQL문을 작성해주세요. 이때 결과는 아이디 순으로 조회해야 합니다.
-- 시각(시-분-초)을 제외한 날짜(년-월-일)만 보여주세요
SELECT ANIMAL_ID, NAME, DATE_FORMAT(DATETIME, '%Y-%m-%d') '날짜'
FROM ANIMAL_INS
ORDER BY ANIMAL_ID;

ANIMAL_ID	NAME	날짜
A349996	    Sugar	2018-01-22
A350276	    Jewel	2017-08-13
-- -----------------------------------------------------
DATE(expression)
SELECT DATE("2017-06-15 09:34:21") -- 2017-06-15
-- -----------------------------------------------------
DATE_FORMAT(date, format)
SELECT DATE_FORMAT("2017-06-15", "%Y"); -- 2017
SELECT DATE_FORMAT("2017-06-15", "%W %M %e %Y") -- Thursday June 15 2017
SELECT DATE_FORMAT("2017-06-15", "%M %d %Y"); -- June 15 2017

Format
%a	Abbreviated weekday name (Sun to Sat)
%b	Abbreviated month name (Jan to Dec)
%c	Numeric month name (0 to 12)
%D	Day of the month as a numeric value, followed by suffix (1st, 2nd, 3rd, ...)
%d	Day of the month as a numeric value (01 to 31)
%e	Day of the month as a numeric value (0 to 31)
%f	Microseconds (000000 to 999999)
%H	Hour (00 to 23)
%h	Hour (00 to 12)
%I	Hour (00 to 12)
%i	Minutes (00 to 59)
%j	Day of the year (001 to 366)
%k	Hour (0 to 23)
%l	Hour (1 to 12)
%M	Month name in full (January to December)
%m	Month name as a numeric value (00 to 12)
%p	AM or PM
%r	Time in 12 hour AM or PM format (hh:mm:ss AM/PM)
%S	Seconds (00 to 59)
%s	Seconds (00 to 59)
%T	Time in 24 hour format (hh:mm:ss)
%U	Week where Sunday is the first day of the week (00 to 53)
%u	Week where Monday is the first day of the week (00 to 53)
%V	Week where Sunday is the first day of the week (01 to 53). Used with %X
%v	Week where Monday is the first day of the week (01 to 53). Used with %x
%W	Weekday name in full (Sunday to Saturday)
%w	Day of the week where Sunday=0 and Saturday=6
%X	Year for the week where Sunday is the first day of the week. Used with %V
%x	Year for the week where Monday is the first day of the week. Used with %v
%Y	Year as a numeric, 4-digit value
%y	Year as a numeric, 2-digit value