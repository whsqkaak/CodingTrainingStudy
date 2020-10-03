    from collections import deque
    import math

    def solution(progresses, speeds):
        answer = []
        need_days = deque(map(lambda x, y:math.ceil((100 - y)/x), speeds, progresses))

        while len(need_days) != 0:
            sum = 1
            ptr = need_days.popleft()
            need_days = deque(map(lambda x:x-ptr, need_days))

            while len(need_days) != 0:
                if need_days[0] <= 0:
                    sum += 1
                    need_days.popleft()
                else:
                    break
            
            answer.append(sum)
        return answer

if __name__ == "__main__":
    solution([93, 30, 55], [1, 30, 5])