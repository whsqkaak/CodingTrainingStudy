import math
from itertools import permutations

def solution(numbers):
    answer = 0
    all_perm = []
    for i in range(1, len(numbers)+1):
        i_perm = list(permutations(numbers, i))
        for j in i_perm:
            tmp = ""
            for k in j:
                tmp += k

            while tmp[0] == '0':
                tmp = tmp[1:]
                if len(tmp) == 0:
                    break

            if (tmp != '') and not (tmp in all_perm):
                all_perm.append(tmp)
    print(all_perm)
    answer = list(filter(lambda x:is_prime(x), all_perm))
    return answer

def is_prime(x):
    t_x = int(x)
    
    if t_x < 2:
        return False

    x_sqrt = math.sqrt(t_x)

    for i in range(2, int(x_sqrt)+1):
        if t_x % i == 0:
            return False
    
    return True

if __name__ == "__main__":
    print(solution("011"))