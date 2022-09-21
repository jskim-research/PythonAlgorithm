"""
programmers 하샤드 수 풀이

시작 시간: 2022.09.21 10:36
끝 시간: 2022.09.21 10:37
걸린 시간: 1분
병목 원인:
개선 여지:
"""


def solution(x):
    return x % sum([int(c) for c in str(x)]) == 0
