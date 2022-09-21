"""
programmers 약수의합 풀이

시작 시간: 2022.09.21 10:06
끝 시간: 2022.09.21 10:08
걸린 시간: 2분
병목 원인:
개선 여지:
"""


def solution(n):
    return sum([i for i in range(1, n+1) if n % i == 0])
