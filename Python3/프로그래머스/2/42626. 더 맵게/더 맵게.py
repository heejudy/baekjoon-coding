import heapq

def solution(scoville, K):
    answer = 0
    
    heapq.heapify(scoville)
    
    while scoville:
        if scoville[0] >= K:
            break
        
        if len(scoville) < 2:
            return -1
            
        one = heapq.heappop(scoville)
        two = heapq.heappop(scoville)
        
        sum_result = one + (two * 2)
        
        heapq.heappush(scoville, sum_result)
        answer += 1
    
    return answer