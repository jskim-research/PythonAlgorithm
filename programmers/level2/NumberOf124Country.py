"""
programmers 124 나라의 숫자 문제풀이

시작 시간: 2022.07.27 22:39
끝 시간: 2022.07.28 00:24
걸린 시간: 1시간 35분
병목 원인: small case에서 답이 나오는 경우를 내고 나서야 확장 case를 생각하는 것이 맞는 것 같음
개선 방법:
"""

# 자리 개수 알면 n - base => 큰 값 자릿수부터 (3^m) 최대한 가져가기
import math
from collections import deque


def transform_124(n: int):
    """10진수를 124 나라의 숫자로 변환"""
    answer = ''
    base, digit = get_base(n)
    remain = n - base
    to_124 = ['1', '1', '2', '4']
    pow_list = [1]
    for _ in range(digit):
        pow_list.append(pow_list[-1] * 3)

    for d in range(digit, 0, -1):
        p = pow_list[d - 1]
        answer += to_124[int(1 + remain // p)]
        remain %= p
    return answer


def get_base(target, base=1, digit=1):
    if target < base:
        return (base - 1) // 3, digit - 1
    return get_base(target, 1 + base * 3, digit + 1)


def solution(n):
    answer = transform_124(n)
    return answer

