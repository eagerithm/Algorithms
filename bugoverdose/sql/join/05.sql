-- Summer/Winter Coding(2019) - 우유와 요거트가 담긴 장바구니
-- 우유와 요거트를 동시에 구입한 장바구니의 아이디를 조회하는 SQL 문을 작성해주세요. 이때 결과는 장바구니의 아이디 순으로 나와야 합니다.

SELECT A.CART_ID
FROM CART_PRODUCTS A INNER JOIN CART_PRODUCTS B
ON A.CART_ID = B.CART_ID
WHERE A.NAME = "Milk" and B.NAME = "Yogurt"
GROUP BY CART_ID
ORDER BY A.CART_ID

-- -------------------------------------------------------------