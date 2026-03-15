def solution(bandage, health, attacks):
    answer = 0
    
    full_health = health
    ing = bandage[0]
    ing_count = 0
    persec = bandage[1]
    addblood = bandage[2]
    
    # 마지막 공격 시간 동안 반복함
    for time in range(1, attacks[-1][0] + 1):
        # 공격 체크 
        # 지금의 시간이 공격 받는 시간과 같다면, 현재 체력에서 공격량을 뺴줌 and 연속 성공 = 0
        if time == attacks[0][0]:
            health -= attacks[0][1]
            ing_count = 0
            if health <= 0:
                return -1 
            attacks.pop(0)
        # 지금의 시간이 공격 받는 시간과 다르다면, 체력을 더해줌 
        else:
            ing_count += 1
            health += persec 
            if ing_count == ing:
                health += addblood
                ing_count = 0
            if health > full_health: 
                health = full_health        

            
    return health
