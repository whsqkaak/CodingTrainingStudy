def solution(people, limit):
    answer = 0
    people.sort()
    left = 0
    right = len(people) - 1

    while right - left > 0:
        if people[left] + people[right] > limit:
            right -= 1
        
        else:
            left += 1
            right -= 1
        
        answer += 1

    if left == right:
        answer += 1
    return answer

if __name__ == "__main__":
    print(solution([20, 50, 50, 80], 100))