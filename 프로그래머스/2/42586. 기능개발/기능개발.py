def solution(progresses, speeds):
    answer = []
    days = []  # 각 작업이 완료되는데 필요한 일수를 저장할 리스트
    
    # 각 작업별로 완료까지 필요한 일수 계산
    for i in range(len(progresses)):
        # (100 - 현재진도) / 작업속도를 올림하여 필요한 일수 계산
        if (100 - progresses[i]) % speeds[i] == 0:
            days.append((100 - progresses[i]) // speeds[i])
        else:
            days.append((100 - progresses[i]) // speeds[i] + 1)
    
    # 배포 가능한 기능 개수 계산
    count = 1  # 현재 배포할 기능 개수
    max_day = days[0]  # 현재 배포 기준이 되는 일수
    
    # 두 번째 작업부터 순차적으로 확인
    for i in range(1, len(days)):
        if max_day >= days[i]:  # 현재 작업이 이전 작업과 함께 배포 가능한 경우
            count += 1
        else:  # 새로운 배포가 필요한 경우
            answer.append(count)  # 이전까지의 배포 개수 저장
            count = 1  # 카운트 초기화
            max_day = days[i]  # 새로운 배포 기준일 설정
    
    answer.append(count)  # 마지막 배포 개수 추가
    return answer