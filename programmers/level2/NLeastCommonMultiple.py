"""
programmers N개의 최소공배수 풀이

시작 시간: 2022.09.21 18:14
끝 시간: 2022.09.21
걸린 시간: 다른 답안 참조함
병목 원인: N개의 최소공배수는 2개씩 묶어서 계속 최소공배수를 구한 것과 같다.
개선 여지: lcm(lcm(n1, n2), n3)... 계속 전체적인 최소공배수가 나올 것임을 small case부터 봤으면 좋았을 것
"""
import math


def get_lcm(n1: int, n2: int):
    """두 정수간 최소공배수 (least common multiple) 구하기"""
    gcd = math.gcd(n1, n2)
    lcm = n1 // gcd * n2 // gcd * gcd
    return lcm


def solution(arr):
    lcm = arr[0]
    for i in range(1, len(arr)):
        lcm = get_lcm(lcm, arr[i])
    return lcm