# 가격이 제일 비싼 식품의 정보 출력하기

SELECT PRODUCT_ID,
       PRODUCT_NAME,
       PRODUCT_CD,
       CATEGORY,
       PRICE
from FOOD_PRODUCT
order by price desc  # order by 절로 desc(내림차순 정렬)
limit 1              # 가장 첫 번째 행 하나만 출력하게 limit 1로 제한

