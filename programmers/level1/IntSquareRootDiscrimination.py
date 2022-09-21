"""
programmers 정수 제곱근 판별 풀이

시작 시간: 2022.09.21 10:17
끝 시간: 2022.09.21 10:20
걸린 시간: 3분
병목 원인:
개선 여지:
"""
import math


def solution(n):
    return -1 if math.sqrt(n) % 1 != 0 else (int(math.sqrt(n)) + 1)**2
