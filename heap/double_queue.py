import heapq

def solution(operations):
    q = []
    for operation in operations:
        if operation[0] == "I":
            # input
            input_num = int(operation[2:])
            heapq.heappush(q, input_num)
            
        else:
            # delete
            if q == []:
                continue
            
            if operation[2] == "1":
                # 최댓값 삭제
                del q[-1]
            else:
                # 최솟값 삭제
                del q[0]
    
    if q == []:
        return [0, 0]
    
    return [max(q), min(q)]