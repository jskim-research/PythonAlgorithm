"""
programmers 점프와 순간이동 풀이

시작 시간: 2022.09.22 13:41
끝 시간: 2022.09.22 14:40
걸린 시간: 59분
병목 원인: 아래에서 위로 가는 것만 생각했는데 위에서 아래로 가는걸로 바꾸면 굉장히 쉬워짐 (greedy)
개선 여지:
"""


def solution(n):
    answer = 0
    while n > 0:
        if n % 2 == 0:
            n = n // 2
        else:
            n = n - 1
            answer += 1
    return answer


