def solution(record):
    answer = []
    chat = {}
    
    for i in record:
        record_status = i.split()
        if record_status[0] == 'Enter':
            user_id, name = record_status[1], record_status[2]
            chat[user_id] = name
        # 지우면 에러 남 
        elif record_status[0] == 'Leave':
            user_id = record_status[1]
        else:
            user_id, name = record_status[1], record_status[2]
            chat[user_id] = name
            
    for i in record:
        record_status = i.split()
        user_id = record_status[1]
        name = chat[user_id]
        if record_status[0] == "Enter":
            answer.append(f"{name}님이 들어왔습니다.")
        elif record_status[0] == "Leave":
            answer.append(f"{name}님이 나갔습니다.")

    return answer