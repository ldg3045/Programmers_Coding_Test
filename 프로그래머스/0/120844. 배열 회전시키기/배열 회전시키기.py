# 정수가 담긴 배열 numbers와 문자열 direction가 매개변수로 주어집니다. 
# 배열 numbers의 원소를 direction방향으로 한 칸씩 회전시킨 배열을 
# return하도록 solution 함수를 완성해주세요.

#제한사항
# 3 ≤ numbers의 길이 ≤ 20
# direction은 "left" 와 "right" 둘 중 하나입니다.

def solution(numbers, direction): 
    if direction == "right":
        return [numbers[-1]] + numbers[:-1] # 마지막 원소 + 뒤에서 첫 원소를 제외한 배열 
    else: 
        return numbers[1:] + [numbers[0]] # 1번째부터 마지막까지 배열 + 첫 원소


# 예시
print(solution([1, 2, 3, 4, 5], "right")) # [5, 1, 2, 3, 4]
print(solution([123, 5, 8,10], "left")) # [5, 8, 10, 123]