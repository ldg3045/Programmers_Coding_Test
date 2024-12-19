# FISH_INFO 테이블에서 잡은 물고기 중 
# 가장 큰 물고기의 길이를 'cm' 를 붙여 출력하는 SQL 문을 작성해주세요.

# 이 때 컬럼명은 'MAX_LENGTH' 로 지정해주세요.

      # CONCAT() 함수로 문자열을 결합   컬럼명을 MAX_LENGTH로 지정
SELECT  CONCAT(MAX(LENGTH), 'cm') AS MAX_LENGTH 
             # MAX() 함수로 물고기 중 가장 긴 길이를 산출 후 'cm'출력
              
    FROM   FISH_INFO 