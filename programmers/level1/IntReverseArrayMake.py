"""
programmers 자연수 뒤집어 배열로 만들기 풀이

시작 시간: 2022.09.21 10:22
끝 시간: 2022.09.21 10:23
걸린 시간: 1분
병목 원인:
개선 여지:
"""


def solution(n):
    # map(list, map(reversed, str(n)) 이 더 깔끔한듯
    return list(reversed([int(i) for i in str(n)]))




