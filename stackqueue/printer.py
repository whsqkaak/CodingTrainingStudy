from collections import deque

def solution(priorities, location):
    answer = 0
    deque_priorities = deque(priorities)

    while len(deque_priorities) > 0:
        max_priority = max(deque_priorities)
        j = deque_priorities.popleft()
        
        location -= 1
        if j < max_priority:
            deque_priorities.append(j)

            if location < 0:
                location = len(deque_priorities) - 1

        else:
            answer += 1
            if location < 0:
                return answer
    return answer

if __name__ == "__main__":
    print(solution([2,1,3,2], 2))