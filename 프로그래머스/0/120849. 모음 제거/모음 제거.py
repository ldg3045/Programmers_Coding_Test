# 모음 제거

# 영어에선 a, e, i, o, u 다섯 가지 알파벳을 모음으로 분류합니다.
# 문자열 my_string이 매개변수로 주어질 때 
# 모음을 제거한 문자열을 return하도록 solution 함수를 완성해주세요.

#입출력 예시 : "bus", "nice to meet you"

import re        # re라는 '정규 표현식' 모듈을 불러온다.

def solution(my_string):     # my_string(문자열)을 입력 받도록 함수를 정의한다.
    answer = re.sub('[aeiou]','',my_string) # (a를, b로 바꿈, 가져올 대상)
    return answer     #re.sub는 문자열 중에 일치하는 문자를 공백으로 치환한다.

print(solution("bus\nnice to meet you")) # 사이에 \n 으로 줄바꿈 했다.

#  bs
#  nc t mt y

