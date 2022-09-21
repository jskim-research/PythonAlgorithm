"""
programmers 카펫 풀이

시작 시간: 2022.09.21 15:56
끝 시간: 2022.09.21 14:05
걸린 시간: 9분
병목 원인:
개선 여지:
"""


def solution(brown, yellow):
    n = brown + yellow

    for w in range(n, 0, -1):
        if n % w == 0:
            h = n // w
            brown_num = 2 * w + 2 * h - 4
            if brown_num == brown:
                return [w, h]
    return -1

