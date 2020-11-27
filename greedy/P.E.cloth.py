def solution(n, lost, reserve):
    answer = n
    losted = lost.copy()
    for num in lost:
        if num in reserve:
            losted.remove(num)
            reserve.remove(num)
    
    for num in losted:
        if num-1 in reserve:
            reserve.remove(num-1)
        elif num+1 in reserve:
            reserve.remove(num+1)
        else:
            answer -= 1
            
    return answer