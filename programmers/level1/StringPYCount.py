"""
programmers 문자열 내 p와 y의 개수 풀이

시작 시간: 2022.09.21 10:29
끝 시간: 2022.09.21 10:31
걸린 시간: 2분
병목 원인:
개선 여지:
"""


def solution(s):
    return sum([1 for c in s.lower() if c == 'p']) == sum([1 for c in s.lower() if c == 'y'])

