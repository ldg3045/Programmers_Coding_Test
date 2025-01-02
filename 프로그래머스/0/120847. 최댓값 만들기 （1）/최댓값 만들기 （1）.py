# 최댓값 만들기 (1)
# numbers의 원소 중 두 개를 곱해 만들 수 있는 최댓값을 return하도록 solution 함수를 완성해주세요.

def solution(numbers):
    numbers.sort() # sort() 함수로 리스트를 오름차순 정렬
    return numbers[-1] * numbers[-2] # 마지막 두 개의 원소를 곱해서 최대값을 출력