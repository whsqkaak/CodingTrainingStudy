def solution(n, computers):
    answer = []

    for i in range(n):
        def solution2(computer, k, res_list):
            for j in range(n):
                if j in res_list or True in list(map(lambda x:j in x, answer)):
                    continue
                
                elif k == j:
                    res_list += [j]
                
                elif computer[j] == 1:
                    res_list = solution2(computers[j], j, res_list)
            return res_list

        answer += [solution2(computers[i], i, [])]
        
    answer = list(filter(lambda x:x != [], answer))
    return len(answer)

if __name__ == "__main__":
    print(solution(3,[[1, 1, 0], [1, 1, 1], [0, 1, 1]]))