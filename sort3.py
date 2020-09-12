def solution(citations):
    answer = 0
    for i in citations:
        tmp = len(list(filter(lambda x :x >= i, citations)))
        print("i : ", i)
        print("tmp : ", tmp)
        if i >= tmp and tmp > answer:
            answer = tmp
    return answer

if __name__=="__main__":
    print(solution([3, 0, 6, 1, 5]))