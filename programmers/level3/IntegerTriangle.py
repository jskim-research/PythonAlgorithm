"""
programmers 정수 삼각형 문제풀이

시작 시간: 2022.09.13 16:55
끝 시간: 2022.09.13 17:15
걸린 시간: 20분
병목 원인: 재귀처럼 다수의 배열을 쓰지 않고도 풀 수 있는 문제인데 너무 오버했음
개선 방법:
"""


def dp(visit, d, n, i, j):
    if i < 0 or j < 0 or i < j:
        return 0
    if visit[i][j]:
        return d[i][j]
    d[i][j] = n[i][j] + max(dp(visit, d, n, i - 1, j - 1), dp(visit, d, n, i - 1, j))
    visit[i][j] = True
    return d[i][j]


def solution(triangle):
    answer = 0
    visit = [[False] * len(l) for l in triangle]
    d = [[0] * len(l) for l in triangle]

    N = len(triangle)
    for i in range(N):
        answer = max(answer, dp(visit, d, triangle, N - 1, i))
    return answer

