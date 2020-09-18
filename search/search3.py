import math

def solution(brown, yellow):
    answer = []
    size = brown + yellow

    for i in range(3, int(math.sqrt(size)) + 1):
        if size % i == 0:
            val = int(size / i)
            if val >= 3 and yellow == (val-2)*(i-2):
                answer = [val, i]
                return answer
    return answer

if __name__ == "__main__":
    print(solution(24, 24))