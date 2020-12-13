from collections import deque

def solution(n, edge):
    answer = 0
    distances = dict(map(lambda x : (x, 0), range(1, n+1)))
    
    # 각 그래프의 연결 상태
    connections = dict(map(lambda x : (x, []), range(1, n+1)))
    
    for e in edge:
        connections[e[0]].append(e[1])
        connections[e[1]].append(e[0])
    
    q = deque(connections[1])
    d = 1
    while q:
        for _ in range(len(q)):
            first = q.popleft()
            
            if distances[first] == 0:
                distances[first] = d

                for node in connections[first]:
                    # if node not in q:
                    q.append(node)
        d += 1
    
    # 1에 대한 것은 필요없으니 0으로 초기화
    distances[1] = 0

    max_distance = max(distances.values())
    for distance in distances.values():
        if distance == max_distance:
            answer += 1

    return answer
