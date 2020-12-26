def solution(N, number):

    possible_nums = []

    tmp_N = N
    # 각각 N을 i번 사용했을 때 가능한 경우의 수들
    for N_num in range(1, 9):

        tmp = set()

        tmp.add(tmp_N)
        # N = N * 10 + N
        tmp_N = tmp_N * 10 + N
        for i in range(len(possible_nums)):

            j = N_num - (i+1) - 1
            i_nums = possible_nums[i]
            j_nums = possible_nums[j]

            for i_num in i_nums:

                for j_num in j_nums:

                    tmp.add(i_num+j_num)
                    tmp.add(i_num-j_num)
                    tmp.add(i_num*j_num)

                    if j_num != 0:
                        tmp.add(int(i_num/j_num))

        if number in tmp:
            return N_num

        possible_nums.append(tmp)

    return -1

if __name__ == "__main__":
    print(solution(5, 1))
