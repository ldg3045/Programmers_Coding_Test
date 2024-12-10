# 상위 n개 레코드

# ANIMAL_INS 테이블에서 가장 먼저 들어온 동물(NAME)의 이름을 조회합니다.
SELECT NAME
FROM ANIMAL_INS

# ORDER BY절을 사용해 DATETIME열 기준으로 날짜를 정렬
ORDER BY DATETIME ASC # ASC : 오름차순(최소값부터) 정렬
LIMIT 1               # 가장 먼저 정렬된 데이터 중 첫 번째 행만 반환