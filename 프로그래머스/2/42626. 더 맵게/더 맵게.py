import heapq

def solution(scoville, K):
    heapq.heapify(scoville)
    first = 0
    cnt = 0
    while scoville[0] < K:
        if len(scoville) < 2:
            return -1
        first = heapq.heappop(scoville)
        second = heapq.heappop(scoville)

        heapq.heappush(scoville, first+(second*2))
        cnt += 1
        
    return cnt
    