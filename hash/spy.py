def solution(clothes):
    answer = 1
    cloth_types = dict()
    
    for cloth in clothes:
        if cloth[1] in cloth_types:
            cloth_types[cloth[1]] += 1
        else:
            cloth_types[cloth[1]] = 1
            
    for cloth_type in cloth_types:
        answer *= cloth_types[cloth_type] + 1
    answer -= 1
    return answer