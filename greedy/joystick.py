def solution(name):
    answer = 0
    ptr = 0
    original = 'A' * len(name)

    while name != original:
        if name[ptr] != original[ptr]:
            diff = abs(ord(name[ptr]) - ord(original[ptr]))
            answer += min(diff, 26-diff)
            tmp = ptr
            if ptr < 0:
                tmp = len(name) + ptr
            original = original[:tmp] + name[tmp] + original[tmp+1:]

        print(name)
        print(original[:10])
        if name == original:
            break

        if ptr - 1 <= -len(name):
            left = len(name) - 1
        else:
            left = ptr - 1

        if ptr + 1 >= len(name):
            right = 0
        else:
            right = ptr + 1

        while name[left] == original[left] and name[right] == original[right]:
            if left <= -len(name):
                left = len(name) - 1
            else:
                left = left - 1

            if right + 1 >= len(name):
                right = 0
            else:
                right = right + 1
            
        
        if name[right] != original[right]:
            if right < ptr:
                answer += len(name) - abs(ptr - right)
            else:
                answer += abs(ptr - right)
            ptr = right

        else:
            if left > ptr:
                answer += len(name) - abs(ptr - left)
            else:
                answer += abs(ptr - left)
            ptr = left

    return answer

if __name__ == "__main__":
    print(solution("JAN"))