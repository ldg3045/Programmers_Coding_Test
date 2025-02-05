def solution(s):

    s = s.split() # 공백을 기준으로 나누기
    for i in range(len(s)):
        if 'Z' in s:
            if s[i] == 'Z':
                s[i] = '0' # 문자열 0 으로 변환
                s[i-1] = '0'

    answer= sum(int(num) for num in s) # 정수로 변환하고 더함
    return answer

