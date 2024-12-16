# - DATETIME에서 DATE로 형 변환

# ANIMAL_INS 테이블에 등록된 동물의 아이디와 이름, 
# 들어온 날짜를 조회 후 아이디 순으로 조회

SELECT ANIMAL_ID,       # 아이디 순으로 기준
       NAME,            # 이름
       DATE_FORMAT(DATETIME, '%Y-%m-%d') AS 날짜 
       # DATE_FORMAT 함수로 DATETIME중 시간은 빼고,
       # 날짜만 포맷팅 시켜, 문자열 '%Y-%m-%d'로 변환
from ANIMAL_INS

# ANIMAL_ID	 NAME	날짜
# A349996	 Sugar	2018-01-22
# A350276	 Jewel	2017-08-13
# A350375	 Meo	2017-03-06
