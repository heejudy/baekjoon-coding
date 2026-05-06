def solution(s):
    total_zero = 0
    cnt = 0
    
    def change(num):
        result = ""
        while num != 1:
            result += str(num % 2)
            num = num // 2
        result += "1"
        return result[::-1]
        
    while s != "1":
        cnt_zero = s.count("0")
        cnt += 1
        if cnt_zero:
            total_zero += cnt_zero
            cnt_one = len(s) - cnt_zero
            s = change(cnt_one)
        else:
            s = change(len(s))

    return [cnt, total_zero]