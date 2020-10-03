from collections import deque

def solution(prices):
    answer = []
    
    queue = deque(prices)

    while len(queue) != 0:
        num = 0
        now = queue.popleft()
        for price in queue:
            num += 1
            if now > price:
                break
        answer += [num]

    # for i in range(len(prices)):
    #     num = 0
    #     for price in prices[i+1:]:
    #         num += 1
    #         if prices[i] > price:
    #             break
    #     answer += [num]
    return answer