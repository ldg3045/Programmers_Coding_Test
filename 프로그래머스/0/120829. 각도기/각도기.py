# 각에서 0도 초과 90도 미만은 예각(1), 90도는 직각(2), 
# 90도 초과 180도 미만은 둔각(3), 180도는 평각(4)으로 분류하세요

def solution(angle):
    answer = 0 
    if angle > 0 and angle < 90:
        answer = 1
    elif angle == 90:
        answer = 2
    elif angle > 90 and angle < 180:
        answer = 3
    elif angle == 180:
        answer = 4
    return answer

print(solution(80))
# 1