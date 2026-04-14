def solution(schedules, timelogs, startday):
    answer = len(schedules)
    # 주말은 상관 X 
    weekend = 6 - startday
    # 직원들 수만큼 반복
    for i in range(len(schedules)):
        # limit = 출근해야하는 시간 
        #만약 schedules[i]의 값이 50이상이라면 그에 따른 코드 필요함 
        if int(str(schedules[i])[-2:]) >= 50:
            limit = schedules[i] + 50
        else:
            limit = schedules[i] + 10
        # 직원 한 명 씩 timelog 꺼내옴
        timelog = timelogs[i]
        # 주말은 limit로 설정하여 그냥 통과하도록 함
        timelog[weekend] = limit
        timelog[weekend + 1] = limit
        # 직원의 일주일 timelog들을 검사함 
        for time in timelog:
            # 출근 시간이 limit보다 크다면 
            if time > limit:
                answer -= 1
                break

        
    return answer