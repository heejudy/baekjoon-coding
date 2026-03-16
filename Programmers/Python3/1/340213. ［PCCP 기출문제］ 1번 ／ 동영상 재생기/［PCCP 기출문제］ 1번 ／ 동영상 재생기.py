def solution(video_len, pos, op_start, op_end, commands):
    answer = ''
    
    def cur_min(time):
        return int(time[0:2])
    def cur_sec(time):
        return int(time[3:5])
    def to_sec(time):
        return cur_min(time) * 60 + cur_sec(time)
        
    answer_time = to_sec(pos)
    video_sec = to_sec(video_len)
    op_st = to_sec(op_start)
    op_e = to_sec(op_end)
    
    for i in commands:
        if answer_time >= op_st and answer_time <= op_e:
            answer_time = op_e
        if i == "next":
            if answer_time <= video_sec - 10:
                answer_time += 10
            else:
                answer_time = video_sec
        if i == "prev":
            if answer_time >= 10:
                answer_time -= 10
            else:
                answer_time = 0
      
    if answer_time >= op_st and answer_time <= op_e:
            answer_time = op_e
    
    # int 형식의 초를 지정된 형식으로 바꾸기 
    res_min = answer_time // 60
    res_sec = answer_time % 60 
    if res_min < 10: 
        res_min = f'0{res_min}'
    if res_sec < 10: 
        res_sec = f'0{res_sec}'
    answer = f"{res_min}:{res_sec}"
        
    
    return answer