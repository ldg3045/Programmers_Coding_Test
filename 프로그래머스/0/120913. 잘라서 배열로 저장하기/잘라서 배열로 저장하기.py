# 잘라서 배열로 저장하기

# 문자열 my_str과 n이 매개변수로 주어질 때,
# my_str을 길이 n씩 잘라서 저장한 배열을 return하도록 solution 함수를 완성해주세요.

def solution(my_str, n): # my_str : 문자열, n : 정수
    answer = []        
    for i in range(0, len(my_str), n): # 0부터 my_str의 길이까지 n씩 잘라서 배열에 저장
        answer.append(my_str[i:i+n]) # i부터 i+n까지 append로 추가
    return answer

print(solution("abc1Addfggg4556b", 6)) # 출력 : ['abc1Ad', 'dfggg4', '556b']