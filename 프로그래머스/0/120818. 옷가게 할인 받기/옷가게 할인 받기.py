def solution(price):
    if price >= 500000:
        return int(price * 0.8) # 소수점 이하를 버린 정수
    elif price >= 300000:
        return int(price * 0.9) # 정수로 리턴
    elif price >= 100000:
        return int(price * 0.95)
    else:
        return price
    
    
print(solution(150000)) 