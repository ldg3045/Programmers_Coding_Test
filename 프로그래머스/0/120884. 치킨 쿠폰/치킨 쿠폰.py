def solution(chicken):
    service_chicken = 0  # 서비스 치킨 수
    coupon = chicken  # 쿠폰 수
    while coupon >= 10: # 쿠폰이 10장 이상이면 서비스 치킨 제공
        service_chicken += coupon // 10  # 10으로 나눈 몫을 서비스 치킨 수에 더함
        coupon = coupon // 10 + coupon % 10  # 쿠폰도 10으로 나눈 몫에 + 나머지를 더함
    return service_chicken # 서비스 치킨 수 반환

print(solution(100)) # 서비스 치킨 11마리
