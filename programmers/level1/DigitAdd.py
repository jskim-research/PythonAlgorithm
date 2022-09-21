"""
programmers 자릿수 더하기 풀이

시작 시간: 2022.09.21 10:11
끝 시간: 2022.09.21 10:12
걸린 시간: 1분
병목 원인:
개선 여지:
"""


def solution(n):
    return sum([int(c) for c in str(n)])

