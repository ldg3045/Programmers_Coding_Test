# 동물 보호소에 가장 먼저 들어온 동물은 언제 들어왔는지 조회하는 SQL 문을 작성해주세요.

SELECT MIN(DATETIME) as '시간'
FROM ANIMAL_INS

# DATETIME의 최소값을 조회

# 시간
# 2013-10-14 15:38:00