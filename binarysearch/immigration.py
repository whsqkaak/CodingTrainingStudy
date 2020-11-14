def solution(n, times):
    times.sort()
    left = 0
    right = times[-1] * n
    answer = (left + right) // 2
    
    while(left <= right):
        tmp = 0
        mid = (left + right) // 2

        for time in times:
            tmp += mid // time

        if tmp < n:
            left = mid + 1
        else:
            answer = min(answer, mid)
            right = mid - 1
    
    return answer