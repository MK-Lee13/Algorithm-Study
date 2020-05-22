import heapq
def solution(scoville, K):
    answer = 0
    h = []
    for scov in scoville:
        heapq.heappush(h, scov)
    while h[0] < K:
        if (len(h) == 1):
            return -1
        a = heapq.heappop(h)
        b = heapq.heappop(h)
        heapq.heappush(h, a + b*2)
        answer += 1
    return answer