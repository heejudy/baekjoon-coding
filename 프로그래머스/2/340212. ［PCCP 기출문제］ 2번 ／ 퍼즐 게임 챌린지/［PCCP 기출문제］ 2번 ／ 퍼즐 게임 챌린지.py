def solution(diffs, times, limit):
    
    def check(diffs, times, mid):
        result = 0
        for i in range(len(diffs)):
            if diffs[i] <= mid: 
                result += times[i]
            else:
                if i > 0: 
                    result += ((times[i-1] + times[i]) * (diffs[i] - mid)) + times[i]
                else: 
                    result += ((times[i]) * (diffs[i] - mid)) + times[i]
        return result
    
    start = min(diffs)
    end = max(diffs)
    while start < end:
        middle = (start + end) // 2
        if check(diffs, times, middle) <= limit:
            end = middle
        else:
            start = middle + 1
            
    return start