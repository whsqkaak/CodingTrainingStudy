def solution(clothes):
    answer = len(clothes)
    cloth_types = dict()
    
    for cloth in clothes:
        if cloth[1] in cloth_types:
            cloth_types[cloth[1]] += 1
        else:
            cloth_types[cloth[1]] = 1
    print(cloth_types)
    tmp = 1
    for cloth_type in cloth_types:
        tmp *= cloth_types[cloth_type]
    answer += tmp
    return answer

if __name__ == "__main__":
    print(solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]))