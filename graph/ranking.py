def solution(n, results):
    # result_matrix : 경기 결과를 담은 매트릭스, {선수 번호 : {선수번호 : 경기 결과,},} 형식으로 이루어진다
    # 경기 결과는 해당 번호의 선수에 대해 1이면 승리, 0이면 알 수 없음, -1 이면 패배이다. 자기 자신은  0
    # ex : (n = 3) {1 : {1 : 0, 2 : 1, 3 : 0}, 2 : {1 : -1, 2 : 0, 3 : 0}, 3 : {1 : 0, 2 : 0, 3 : 0}}
    answer = 0
    result_matrix = dict(map(lambda x : (x, 0), range(1, n+1)))
    result_matrix = dict(map(lambda x : (x, result_matrix.copy()), range(1, n+1)))
    
    for result in results:
        winner = result[0]
        loser = result[1]
        result_matrix[winner][loser] = 1
        result_matrix[loser][winner] = -1
        
        # 연계
        for i in range(1, n+1):
            # 승자를 이긴 선수가 존재할 때
            if result_matrix[winner][i] == -1:
                result_matrix[loser][i] = -1
                result_matrix[i][loser] = 1

                for j in range(1, n+1):
                    if i != j and j != loser and result_matrix[i][j] == 0 and result_matrix[loser][j] != -1:
                        result_matrix[i][j] = result_matrix[loser][j]
            
            # 패자에게 진 선수가 존재할 때
            if result_matrix[loser][i] == 1:
                result_matrix[winner][i] = 1
                result_matrix[i][winner] = -1

                for j in range(1, n+1):
                    if i != j and j != winner and result_matrix[i][j] == 0 and result_matrix[winner][j] != 1:
                        result_matrix[i][j] = result_matrix[winner][j]
            
        
    # 합산
    # result_matrix에 0이 존재하는 선수는 순위를 알 수 없다
    # 0이 존재하지 않는 선수의 개수가 answer(자기 자신을 제외)
    sum_result = [False for _ in range(n)]
    
    for i in range(1, n+1):
        value = list(result_matrix[i].values())
        value.remove(0)
        
        if 0 not in value:
            sum_result[i-1] = True

    answer = len(list(filter(lambda x : x, sum_result)))
    return answer
