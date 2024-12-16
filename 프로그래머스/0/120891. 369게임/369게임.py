# - 369게임
# order가 매개변수로 주어질 때, 
# 쳐야할 박수 횟수를 return 하도록 solution 함수를 완성해보세요.

def solution(order):    
    answer = 0    #누적 계산을 시작하기 전, 변수를 0으로 설정
    for 삼육구 in str(order):  # 반복될 값을 문자열로 변환
        if 삼육구 in ["3","6","9"]: # 문자열에 3,6,9,가 있으면
            answer += 1            # +1 씩 누적시킨다
    return answer             # 누적된 값을 변수에 반환시킨다.