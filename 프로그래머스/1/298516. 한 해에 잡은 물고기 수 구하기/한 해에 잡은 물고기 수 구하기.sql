# 한 해에 잡은 물고기 수 구하기

# FISH_INFO 테이블에서 2021년도에 잡은 물고기 수를 출력하는 SQL 문을 작성해주세요.
# 이 때 컬럼명은 'FISH_COUNT' 로 지정해주세요.

#      count()함수로 수를 세고, ↓ 첫번째부터 4글자까지
select count(substring(TIME, 1, 4)) AS FISH_COUNT  
#      YYYY/MM/DD형식으로 저장되어 substring()함수를 사용하여 년도만 잘라낸다.
from FISH_INFO                          
where TIME like '2021%' # where 절에서 like 연산자를 사용해 
                        # time 컬럼의 데이터가 2021년인 것만 필터링한다.
# 출력 결과
# ┌ FISH_COUNT ┐
# └     2      ┘