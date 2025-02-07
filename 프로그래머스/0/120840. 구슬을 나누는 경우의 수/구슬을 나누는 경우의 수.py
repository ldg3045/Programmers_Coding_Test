def solution(balls, share):
    n = balls
    m = share
    
#         n!
#    ──────────── 
#    (n-m)! x m!

    
    #분모
    moo = 1
#     7! 
#   = 7x6x5x4x3x2x1      
    for i in range(n,m,-1):     # '7','6'
        moo *= i # 7x6
#            └> moo = moo * i

    #분자
    ja = 1
#      (7 - 5)! - 5! 
#    =  2 x 1   - 5x4x3x2x1
    for i in range(n-m,0,-1):   # '2','1'
        ja *= i # 2x1
#           └> ja = ja * i


# 분모와 분자에 공통되는 연산 값을 소거함
#       7x6 (소거 5x4x3x2x1)        
#    ────────────────────────   = 42 ÷ 2
#       2x1 (소거 5x4x3x2x1)

    return moo // ja #          = 21

print(solution(7,5))