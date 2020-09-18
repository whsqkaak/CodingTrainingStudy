def solution(answers):
    answer = []
    a = [1, 2, 3, 4, 5]
    b = [2, 1, 2, 3, 2, 4, 2, 5]
    c = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    answer_num = [0, 0, 0]

    for i in range(len(answers)):
        answer_num[0] += (answers[i] == a[i%len(a)])
        answer_num[1] += (answers[i] == b[i%len(b)])
        answer_num[2] += (answers[i] == c[i%len(c)])
    
    max_answer = max(answer_num)
    for i in range(len(answer_num)):
        if answer_num[i] == max_answer:
            answer.append(i+1)
    return answer
