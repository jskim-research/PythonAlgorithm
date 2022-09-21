"""
programmers 정수 내림차순으로 배치하기  풀이

시작 시간: 2022.09.21 10:40
끝 시간: 2022.09.21 10:41
걸린 시간: 1분
병목 원인:
개선 여지:
"""


def solution(n):
    return int("".join(sorted([c for c in str(n)], reverse=True)))

