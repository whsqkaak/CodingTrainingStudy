def solution(numbers, target):
    answer = 0
    tmp = solution_rec(numbers, [])
    print(tmp)
    answer = len(list(filter(lambda x:x == target, tmp)))
    return answer

def solution_rec(numbers, sums):
    if numbers == []:
        return sums
    
    n = numbers[0]
    if sums == []:
        return solution_rec(numbers[1:], [n, -n])

    tmps = [[sums[0]+n, sums[0]-n], [sums[1]+n, sums[1]-n]]
    return solution_rec(numbers[1:], tmps[0]) + solution_rec(numbers[1:], tmps[1])

if __name__ == "__main__":
    print(solution([1, 1, 1, 1, 1], 3))