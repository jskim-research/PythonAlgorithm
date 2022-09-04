"""
programmers 위장 문제풀이

시작 시간: 2022.09.04 23:41
끝 시간: 2022.09.05 1:20
걸린 시간: 1시간 이상 + 다른 tip 참조
병목 원인: 조합 계산에 대해 효율적인 방법을 떠올리지 못했음 (모든 경우의 수 - 1 등..)
개선 방법:

"""
from collections import defaultdict
from itertools import combinations


def solution(clothes):
    answer = 1
    dic = defaultdict(int)
    for cloth_name, cloth_category in clothes:
        dic[cloth_category] += 1
    categories = list(dic.keys())

    for cat in categories:
        answer *= dic[cat] + 1  # + 1 이 핵심. 해당 cat을 아예 안 입고 다른 cat들로 입은 경우가 있으므로 추가해야함
    answer -= 1
    return answer