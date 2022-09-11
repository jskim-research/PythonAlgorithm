"""
programmers JadenCase 문자열 만들기 풀이

시작 시간: 2022.09.11 22:31
끝 시간: 2022.09.11 22:41
걸린 시간: 10분
병목 원인:
개선 여지:
"""


def solution(s):
    return " ".join(list(map(str.capitalize, s.split(" "))))
