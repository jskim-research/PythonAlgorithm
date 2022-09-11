"""
programmers 최솟값 만들기 풀이

시작 시간: 2022.09.11 23:04
끝 시간: 2022.09.11 23:08
걸린 시간:
병목 원인:
개선 여지:
"""


def solution(A,B):
    answer = 0

    A = sorted(A)
    B = sorted(B, reverse=True)

    return sum([a * b for a, b in zip(A, B)])
