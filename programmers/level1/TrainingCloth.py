"""
programmers 체육복 문제풀이

시작 시간: 2022.08.21 20:46
끝 시간: 2022.08.21 21:03
걸린 시간: 17분
병목 원인: 어떤 식으로 짜야 좋을지 고민했음
개선 방법: 문제 풀이에 익숙해져야할듯
"""


def solution(n, lost, reserve):
    answer = 0
    lost = set(lost)
    reserve = set(reserve)
    lost_but_has_reserve = lost & reserve
    reserve -= lost_but_has_reserve
    lost -= lost_but_has_reserve
    select = [-1, 1]

    for i in range(n):
        if (i + 1) in lost:
            for s in select:
                if (i + s + 1) in reserve:
                    lost.remove(i + 1)
                    reserve.remove(i + s + 1)
                    break

    return n - len(lost)

