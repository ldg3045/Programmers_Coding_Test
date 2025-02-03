def solution(keyinput, board):
    answer = []

    x, y = 0, 0 # 기준점
    x_max = board[0] // 2 # 0번째 값을 2로 나눠 가로 최대 이동 거리
    y_max = board[1] // 2 # 1번째 값을 2로 나눠 세로 최대 이동 거리
    for player in keyinput:
        if player == "up" and y < y_max: # up은 y_max보다 작을 때만 이동 가능
            y += 1 # y좌표 1 증가
        elif player == "down" and y > -y_max: # down은 y_max보다 클 때만 이동 가능
            y -= 1 # y좌표 1 감소
        elif player == "left" and x > -x_max: # left는 x_max보다 작을 때만 이동 가능
            x -= 1 # x좌표 1 감소
        elif player == "right" and x < x_max: # right는 x_max보다 클 때만 이동 가능
            x += 1 # x좌표 1 증가

    answer = [x, y] # 최종 좌표 반환
    return answer

keyinput = ["left", "right", "up", "right", "right"] # [-2, 1]
board = [11, 11]

print(solution(keyinput, board))
