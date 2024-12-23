SELECT DR_NAME,       # 의사 이름
       DR_ID,         # 의사 ID
       MCDP_CD,       # 진료과 코드
       DATE_FORMAT(HIRE_YMD, '%Y-%m-%d') AS HIRE_data 
       #  DATE_FORMAT을 써서 고용 날짜를 년,월,일 형식으로 변환
FROM DOCTOR  

WHERE MCDP_CD = 'CS' OR MCDP_CD = 'GS' 
# 진료과 코드가 'CS' (흉부외과) 또는 'GS' (일반외과)인 의사만 선택합니다.

ORDER BY HIRE_YMD DESC, DR_NAME
# 고용 날짜를 기준으로 내림차순 정렬, 같은 날짜일 경우 의사 이름으로 정렬

# ORDER BY: 데이터를 정렬하는 방법을 지정합니다