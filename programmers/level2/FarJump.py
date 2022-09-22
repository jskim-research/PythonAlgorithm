"""
programmers 멀리뛰기 풀이

시작 시간: 2022.09.22 13:32
끝 시간: 2022.09.22 13:38
걸린 시간: 6분
병목 원인:
개선 여지:
"""


def solution(n):
    d = [0] * (n + 1)
    d[0] = 1
    d[1] = 1

    for i in range(2, n + 1):
        d[i] = d[i - 1] + d[i - 2]

    return d[n] % 1234567

