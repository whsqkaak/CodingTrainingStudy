def solution(triangle):
    # 위에서부터 한 층씩 쌓아 내려가기
    # 층별로 반복
    for i in range(len(triangle)):

        # 맨 위층일 때는 추가적으로 더할 필요가 없으니 continue
        if i == 0:
            continue

        # 나머지 층들은 현재 층의 위의 층 정수를 더한 값 중 최댓값을 저장하도록 한다.
        for j in range(i+1):

            # 맨 왼쪽일 때
            if j == 0:
                triangle[i][j] = triangle[i][j] + triangle[i-1][0]

            # 맨 오른쪽일 때
            elif j == i:
                triangle[i][j] = triangle[i][j] + triangle[i-1][i-1]

            # 중간일 때
            else:
                triangle[i][j] = triangle[i][j] + max(triangle[i-1][j-1], triangle[i-1][j])

    # answer는 triangle의 맨 아랫층에 쌓인 값들 중 최댓값이다.
    return max(triangle[-1])