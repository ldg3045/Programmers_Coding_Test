#짝수는 싫어요

def solution(n):               # 숫자 n을 입력하면
    answer = []                # 결과를 저장할 빈 리스트를 생성

              #'range'함수를 사용해 1부터 n+1이 나오면 멈추고 2씩 건너뛴다
    for i in range(1,n+1,2):   # 나온 홀수 값을 i 변수에 하나씩 저장한다.
        answer.append(i)       # 홀수를 하나씩 리스트'answer'에 추가함

    return answer              # 'answer'리스트를 함수 결과로 돌려줌
