"""
programmers 숫자의표현 문제풀이

시작 시간: 2022.09.09 22:44
끝 시간: 2022.09.09 23:27
걸린 시간: 43분
병목 원인: 수학적 공식으로 축약이 가능한데 그 방법을 모름
개선 방법:
"""
import math


def solution(n):
    # (k+1)*i + (k+1)*k/2 = n
    # (k+1)(2i + k) = 2n
    # (k+1)*i
    answer = 0
    for i in range(1, math.ceil(n / 2) + 1):
        for k in range(1, math.ceil(n / i) + 1):
            if ((k + 1) * i + (k + 1) * k / 2) == n:
                answer += 1

    return answer + 1  # add one more case, i == n
