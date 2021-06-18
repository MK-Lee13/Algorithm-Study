def solution(stones, k):
    start = min(stones)
    end = max(stones)
    
    while end >= start:
        # 첫 자리수 와 마지막 자리수 차가 0 이하이면 종료
        mid = (end + start) // 2
        count_flag = 0
        for stone in stones:
            if stone - mid <= 0:
                # 해당 돌을 건널 수 없음 그래서 점프를 뛰는 상황
                count_flag += 1
            else:
                # 해당 돌을 건널 수 있음
                count_flag = 0
            if count_flag >= k:
                # 건널 수 없는 상황
                break
        if count_flag >= k:
            end = mid - 1
        else:
            start = mid + 1
    return start