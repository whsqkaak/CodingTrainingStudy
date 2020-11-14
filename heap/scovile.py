import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)

    while(True):
        if scoville[0] >= K:
            return answer
        
        if len(scoville) <= 1:
            return -1
        
        answer += 1
        a = heapq.heappop(scoville)
        b = heapq.heappop(scoville)

        heapq.heappush(scoville, a + (b*2))