"""
programmers 땅따먹기 풀이

시작 시간: 2022.10.09 21:05
끝 시간: 2022.10.09 21:12
걸린 시간: 7분
병목 원인:
개선 여지:
"""


def solution(land):
    n = len(land)
    max_score = [[0] * 4 for _ in range(n)]

    for i in range(n):
        for j in range(4):
            if i == 0:
                max_score[i][j] = land[i][j]
            else:
                max_score[i][j] = max(max_score[i - 1][:j] + max_score[i - 1][j + 1:]) + land[i][j]
    return max(max_score[n - 1])



