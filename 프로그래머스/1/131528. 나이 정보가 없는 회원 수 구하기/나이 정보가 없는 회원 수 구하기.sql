# 나이 정보가 없는 회원 수 구하기

SELECT COUNT(*) as users #  COUNT(*)은 항목의 갯수를 구하고 NULL 값도 포함한다.
from USER_INFO           #  USER_INFO 테이블에서 가져온다.
where age is NULL        #  조건문으로 age열에 컬럼값이 NULL인값 불러오기