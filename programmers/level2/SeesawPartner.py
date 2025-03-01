"""
programmers 시소 짝꿍

시작 시간: 2025.03.01 21:51
끝 시간: 2025.03.01 22:17
걸린 시간: 26분
병목 원인: 모든 경우의 수 및 중복 등의 엣지 케이스를 제대로 못 챙김
개선 여지: 문제 작성 전에 모든 경우의 수를 따졌는 지, 엣지 케이스를 꼭 고려해보자
        + pair 문제는 combination 을 활용하여 푸는 것이 직관적일 수 있음
"""


def solution(weights):
    dic = {}

    ratio = [2 / 3, 2 / 4, 3 / 2, 3 / 4, 4 / 2, 4 / 3]

    answer = 0
    for w in weights:
        if w in dic:
            dic[w] += 1
        else:
            dic[w] = 1

    for w in weights:
        for r in ratio:
            if w * r in dic:
                answer += dic[w * r]
                # 본인 제외
        answer += dic[w] - 1

    return answer // 2


from itertools import combinations
from collections import Counter


def second_solution(weights):
    ratio = [1, 2 / 3, 2 / 4, 3 / 2, 3 / 4, 4 / 2, 4 / 3]

    # 각 숫자의 count 만 가지고 답을 도출할 수 있으므로 Counter 활용
    w_count = Counter(weights)

    answer = 0

    for w in w_count.values():
        answer += w * (w - 1) / 2

    for a, b in combinations(w_count.keys(), 2):
        for r in ratio:
            if a == r * b:
                print(a, b)
                answer += w_count[a] * w_count[b]
                break

    return answer
