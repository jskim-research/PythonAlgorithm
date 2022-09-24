"""
programmers 가장 먼 노드 풀이

시작 시간: 2022.09.24 17:58
끝 시간: 2022.09.24 18:05
걸린 시간: 7분
병목 원인:
개선 여지:
"""
from collections import deque, defaultdict


def solution(n, edge):
    q = deque()
    conn = defaultdict(list)
    dist = defaultdict(int)

    visit = [False] * n
    for e in edge:
        conn[e[0] - 1].append(e[1] - 1)
        conn[e[1] - 1].append(e[0] - 1)

    q.append(0)
    visit[0] = True
    dist[0] = 0

    while q:
        v = q.popleft()
        for nv in conn[v]:
            if not visit[nv]:
                q.append(nv)
                dist[nv] = dist[v] + 1
                visit[nv] = True

    max_dist = max(dist.values())
    return sum([1 for d in dist.values() if d == max_dist])