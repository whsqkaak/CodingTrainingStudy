import time

def solution(numbers):
    if sum(numbers) == 0:
        return '0'
    numbers = list(map(str, numbers))
    numbers = merge_sort(numbers)

    return ''.join(numbers)

def merge_sort(numbers):
    if len(numbers) <= 1:
        return numbers
    
    mid = len(numbers) // 2
    left = numbers[:mid]
    right = numbers[mid:]

    m_left = merge_sort(left)
    m_right = merge_sort(right)

    return merge(m_left, m_right)

def merge(left, right):
    i = 0
    j = 0
    result = []
    len_l = len(left)
    len_r = len(right)

    while(i < len_l) & (j < len_r):
        l = left[i]
        r = right[j]
        a = l + r
        b = r + l

        if a > b:
            result.append(l)
            i += 1
        else:
            result.append(r)
            j += 1

    while (i < len_l):
        result.append(left[i])
        i += 1

    while (j < len_r):
        result.append(right[j])
        j += 1
    
    return result

if __name__=="__main__":
    start = time.time()
    print(solution([2,20,200]))
    print("WorkingTime: {} sec".format(time.time()-start))