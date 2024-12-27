# 동물 보호소에 들어온 동물 중 고양이와 개가 각각 몇 마리인지 조회하는 SQL문을 작성해주세요. 이때 고양이를 개보다 먼저 조회해주세요.

SELECT ANIMAL_TYPE, COUNT(*) AS count
FROM ANIMAL_INS

GROUP BY ANIMAL_TYPE
HAVING ANIMAL_TYPE IN ('Cat', 'Dog') 
# Cat과 Dog만 있지 않는 경우를 생각하여 HAVING으로 포함 된 문자열 조건 추가
ORDER BY ANIMAL_TYPE