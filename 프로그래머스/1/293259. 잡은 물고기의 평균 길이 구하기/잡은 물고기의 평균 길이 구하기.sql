# 평균 길이는 소수점 3째자리에서 반올림하며, 
# 10cm 이하의 물고기들은 10cm 로 취급하여 평균 길이를 구해주세요.

select round(AVG(IFNULL(LENGTH, 10)),2) as 'AVERAGE_LENGTH'
from FISH_INFO

# ROUND: 계산된 평균값을 소수점 2째자리까지 표시 (3째자리에서 반올림)
# AVG: LENGTH 값들의 평균 계산
# IFNULL: LENGTH 값이 NULL인 경우 10으로 대체

#   ┌ AVERAGE_LENGTH ┐
#   └     26.67      ┘    