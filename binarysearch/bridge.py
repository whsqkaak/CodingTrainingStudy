def solution(distance, rocks, n):
    answer = 0
    rocks.sort()
    all_rocks = rocks.copy()
    all_rocks.append(0)
    all_rocks.append(distance)
    tmp_dist = []

    for t in rocks:
        tmp = list(map(lambda x:abs(x - t), all_rocks))
        tmp.remove(0)
        tmp_dist.append(min(tmp))
    return max(tmp_dist)