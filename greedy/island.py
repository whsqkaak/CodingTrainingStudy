def solution(n, costs):
    """
    크루스칼 알고리즘 적용
    """
    answer = 0

    # costs 기준으로 오름차순 정렬
    costs = sorted(costs, key=lambda x:x[2])
    costs = list(map(lambda x: [x[1], x[0], x[2]] if x[1] < x[0] else x, costs))
    
    # 사이클 테이블
    cycle_table = dict(map(lambda x:[x, x], range(n)))
    
    # 정렬된 순서대로 더하기
    for connect in costs:

        if cycle_table[connect[0]] == cycle_table[connect[1]]:
            continue

        else:
            answer += connect[2]
            tmp = cycle_table[connect[1]]
            
            for i in cycle_table:
                if cycle_table[i] == tmp:
                    cycle_table[i] = cycle_table[connect[0]]

    return answer