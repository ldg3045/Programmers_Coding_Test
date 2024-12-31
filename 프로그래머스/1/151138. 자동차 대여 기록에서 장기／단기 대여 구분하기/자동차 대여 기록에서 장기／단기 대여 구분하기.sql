# '네비게이션' 옵션이 포함된 SQL문을 작성해주세요.
# 결과는 자동차 ID를 기준으로 내림차순 정렬해주세요.

SELECT  HISTORY_ID,
        CAR_ID,
        DATE_FORMAT(START_DATE, '%Y-%m-%d') AS START_DATE,
        DATE_FORMAT(END_DATE, '%Y-%m-%d') AS END_DATE,
        # CASE WHEN: 조건문 시작, THEN: 조건이 참일 때 반환할 값        
        CASE WHEN DATEDIFF(END_DATE,START_DATE) + 1 >= 30 THEN "장기 대여"
        ELSE "단기 대여" END AS RENT_TYPE # 실제 대여일수(시작일 포함) : 30일   
  FROM  CAR_RENTAL_COMPANY_RENTAL_HISTORY
                 # BETWEEN: 두 값 사이의 범위를 지정 
 WHERE  START_DATE BETWEEN '2022-09-01' AND '2022-09-30'
 ORDER BY  HISTORY_ID DESC # DESC(내림차순 정렬)