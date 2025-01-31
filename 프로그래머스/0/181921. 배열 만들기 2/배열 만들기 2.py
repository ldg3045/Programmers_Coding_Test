def solution(l, r):
    answer = [] 
    for i in range(l, r + 1):  # l부터 r까지의 모든 정수에 대해 반복, 끝 값 포함(+1) 필요
        # i를 문자열로 변환한 후, '0'과 '5'를 뺀다
        if set(str(i)) - set(['0', '5']) == set(): # 뺀 결과가 빈 집합이면 조건 만족
            answer.append(i)  # 만족하는 i값을 answer에 추가
    return answer if answer else [-1]  # 만약 그러한 정수가 없다면 None 대신 [-1] 반환

print(solution(5, 555))