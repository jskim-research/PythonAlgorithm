"""
programmers 섬 연결하기 풀이

시작 시간: 2022.09.24 07:50
끝 시간: 2022.09.24 08:44
걸린 시간: 54분
병목 원인: 그래프 알고리즘 (크루스칼 알고리즘)을 파이썬으로 직접 구현해본 적이 없어 방황함
          cycle을 check할 때 parent들이 같은지 확인하고, 연결할 때도 parent를 작은 수를 기준으로 통합
개선 여지:
"""
from collections import defaultdict
from heapq import heappush, heappop


def get_parent(parent, x):
    if parent[x] == x:
        return x
    return get_parent(parent, parent[x])


def union_parent(parent, a, b):
    a = get_parent(parent, a)
    b = get_parent(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b


def solution(n, costs):
    answer = 0
    h = []
    parent = [0] * n

    for i in range(n):
        parent[i] = i

    for cost in costs:
        heappush(h, (cost[2], cost[0], cost[1]))

    while h:
        c, s, e = heappop(h)
        if get_parent(parent, s) != get_parent(parent, e):
            union_parent(parent, s, e)
            answer += c

    return answer

