def solution(spell, dic):
    spell.sort() # 외계어 알파벳 정렬
   # print(spell) # ['d', 'x', 'z']
    for i in dic:
        if spell == sorted(i): # 사전에 외계어 알파벳이 존재한다면
           # print(spell) #  ['d', 'x', 'z']
            return 1
    return 2


print(solution(["z", "d", "x"],["def", "dzx"]))