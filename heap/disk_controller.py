import heapq

def solution(jobs):
    answer, cur_time = 0, 0
    n = len(jobs)
    jobs.sort()

    while jobs:
        if cur_time >= jobs[0][0]:
            # 현재 시간 기준으로 저장된 작업들을 filter
            # 작업 실행 시간 기준으로 오름차순 정렬
            tmp = sorted(list(filter(lambda x: x if x[0] <= cur_time else False, jobs)),key=lambda x: x[1])
            tp = heapq.heappop(tmp)

            cur_time += tp[1]
            answer += cur_time-tp[0]
            
            # 나머지 작업들을 다시 jobs에 저장
            jobs = tmp + jobs[len(tmp)+1:]
        else: 
            # 현재 시간에 저장할 수 있는 작업이 없다면 jobs에서 가장 먼저 처리할 수 있는 job을 받아온다
            cur_time = jobs[0][0]    

    return int(answer/n)
