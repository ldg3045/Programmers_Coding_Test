# '경제' 카테고리에 속하는 도서들의 도서
# ID(BOOK_ID), 저자명(AUTHOR_NAME), 출판일(PUBLISHED_DATE)
# 리스트를 출판일 기준으로 오름차순 정렬해주세요.

SELECT BOOK_ID, AUTHOR_NAME,
       DATE_FORMAT(PUBLISHED_DATE, '%Y-%m-%d') AS PUBLISHED_DATE
FROM BOOK
INNER JOIN AUTHOR # INNER JOIN: 두 테이블에서 조건이 일치하는 행만 결합
# ON: JOIN의 조건으로 AUTHOR_ID와 AUTHOR_ID가 같은 것끼리 연결
ON BOOK.AUTHOR_ID = AUTHOR.AUTHOR_ID
WHERE CATEGORY = '경제'
ORDER BY PUBLISHED_DATE # 출판일 기준으로 정렬

