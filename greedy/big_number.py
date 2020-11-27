def solution(number, k):
    answer = ''
    len_number = len(number)
    number_to_find = len_number - k
    ptr = 0

    while number_to_find > 0:
        max_num = '0'

        for i in range(ptr, len_number - number_to_find+1):
            if number[i] > max_num:
                max_num = number[i]
                ptr = i
                if max_num == '9':
                    break
            
        answer += str(max_num)
        ptr += 1
        number_to_find -= 1

    return answer

if __name__ == "__main__":
    solution("1231234", 3)