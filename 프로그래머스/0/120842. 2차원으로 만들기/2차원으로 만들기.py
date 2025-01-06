def solution(num_list, n):
    answer = [] # 리스트 안에 리스트로 2차원 리스트 만들기
    for i in range(0, len(num_list), n):
        temp = []
        for j in range(0, n):
            temp.append(num_list[i+j])
        answer.append(temp)
    return answer

print(solution([1, 2, 3, 4, 5, 6, 7, 8], 2))