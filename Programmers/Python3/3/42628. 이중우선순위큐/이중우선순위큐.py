import heapq

def solution(operations):

    min_heap = []
    max_heap = []

    visited = {}

    idx = 0

    for i in operations:

        cmd, num = i.split()
        num = int(num)

        # 삽입
        if cmd == "I":

            heapq.heappush(min_heap, (num, idx))
            heapq.heappush(max_heap, (-num, idx))

            visited[idx] = True
            idx += 1

        # 삭제
        else:

            # 최댓값 삭제
            if num == 1:

                while max_heap and not visited[max_heap[0][1]]:
                    heapq.heappop(max_heap)

                if max_heap:
                    visited[max_heap[0][1]] = False
                    heapq.heappop(max_heap)

            # 최솟값 삭제
            else:

                while min_heap and not visited[min_heap[0][1]]:
                    heapq.heappop(min_heap)

                if min_heap:
                    visited[min_heap[0][1]] = False
                    heapq.heappop(min_heap)
                    
    while min_heap and not visited[min_heap[0][1]]:
        heapq.heappop(min_heap)

    while max_heap and not visited[max_heap[0][1]]:
        heapq.heappop(max_heap)

    if not min_heap or not max_heap:
        return [0, 0]

    return [-max_heap[0][0], min_heap[0][0]]