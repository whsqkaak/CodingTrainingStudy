from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 1
    passed_trucks = []
    passing_trucks = deque([])
    waiting_trucks = deque(truck_weights)
    passing_secs = deque([])

    while passed_trucks != truck_weights:
        answer += 1
        if len(waiting_trucks) > 0 and sum(passing_trucks) + waiting_trucks[0] <= weight:
            tmp_truck = waiting_trucks.popleft()

            passing_trucks.append(tmp_truck)
            passing_secs.append(0)

        passing_secs = deque(map(lambda x: x+1, passing_secs))

        while len(passing_secs) > 0 and passing_secs[0] == bridge_length:
            passing_secs.popleft()
            passed_trucks.append(passing_trucks.popleft())

    return answer

if __name__ == "__main__":
    print(solution(2, 10, [7,4,5,6]))