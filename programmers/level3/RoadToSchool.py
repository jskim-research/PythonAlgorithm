"""
programmers 등굣길 풀이

시작 시간: 2022.09.18 22:44
끝 시간: 2022.09.18 23:30
걸린 시간: 46분
병목 원인: 오른쪽, 아래로만 이동이 가능할 때 일단 목적지에 도달만 가능하면 최단거리 라는 사실을 간과함
개선 여지:
"""


def solution(m, n, puddles):
    # 오른쪽, 밑 이동만 가능하기 때문에 도착만 가능하면 최단거리 경우임
    grid = [[0] * (n + 1) for _ in range(m + 1)]  # n+1, m+1을 사용하여 indexing error 방지
    grid[1][1] = 1  # 가장 처음 경우의 수는 1
    for p in puddles:
        grid[p[0]][p[1]] = -1

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if i == j == 1:
                continue
            if grid[i][j] == -1:
                grid[i][j] = 0  # 도달할 수 있는 경우의 수 0
            else:
                grid[i][j] = (grid[i - 1][j] + grid[i][j - 1]) % 1000000007

    return grid[m][n]

