def solution(m, n, puddles):
    answer = 0
    # 모든 값이 0으로 되어 있는 m * n 지도 생성
    maps = [[0 for _ in range(m)] for _ in range(n)]    

    # 물이 차있는 곳은 -1으로 표시
    for puddle in puddles:
        maps[puddle[1]-1][puddle[0]-1] = -1

    # 현재 좌표까지 도달하는 데 가능한 경로는 위쪽 좌표와 왼쪽 좌표를 더한 값
    # 물웅덩이(-1)은 0으로 초기화하고 넘어간다.
    maps[0][0] = 1
    for i in range(n):
        for j in range(m):
            if maps[i][j] == -1:
                maps[i][j] = 0

            else:
                # 위쪽 테두리일 때
                if i == 0 and j != 0:
                    maps[i][j] += maps[i][j-1]

                # 왼쪽 테두리일 때
                elif j == 0:
                    maps[i][j] += maps[i-1][j]

                else:
                    maps[i][j] = (maps[i-1][j] + maps[i][j-1]) % 1000000007

    return maps[n-1][m-1]
