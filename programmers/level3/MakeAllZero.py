"""
programmers 모두 0으로 만들기 풀이

시작 시간: 2022.07.25 ??
끝 시간: 2022.07.26 ??
걸린 시간: 하루 이상 걸림
병목 원인: 최대 재귀 회수 limit 고려 안함 (런타임 에러) +
         어차피 zero-sum 이라서 작은 것부터 움직이지 않고 큰 것부터 움직여도 결과적으론 계산 횟수에 변화가 없음.
         root로 병합만 되면 됨.
개선 여지:
"""

import sys
from collections import defaultdict

sys.setrecursionlimit(10 ** 6)  # 최대 재귀 회수


def dfs(tree, weights, cur_vertex, visit):
    if visit[cur_vertex]:
        return 0, 0
    visit[cur_vertex] = True
    calc_num = 0
    weight = weights[cur_vertex]
    childs = tree[cur_vertex]
    for child in childs:
        _calc_num, _weight = dfs(tree, weights, child, visit)
        calc_num += _calc_num + abs(_weight)
        weight += _weight
    return calc_num, weight


def solution(a, edges):
    answer = 0
    tree = defaultdict(list)

    for edge in edges:
        tree[edge[0]].append(edge[1])
        tree[edge[1]].append(edge[0])

    visit = [False for _ in range(len(a))]

    if sum(a) != 0:  # 0으로 만드는 것이 불가능한 경우
        return -1

    root_vertex = 0
    answer, _ = dfs(tree, a, root_vertex, visit)

    return answer