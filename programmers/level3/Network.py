"""
programmers 네트워크 풀이

시작 시간: 2022.09.20 21:46
끝 시간: 2022.09.20 21:54
걸린 시간:
병목 원인:
개선 여지:
"""
from collections import deque


def bfs(i, visit, connection, n):
    q = deque()
    q.append(i)
    visit[i] = True
    while q:
        i = q.popleft()
        for j in range(0, n):
            if i != j and not visit[j] and connection[i][j]:
                visit[j] = True
                q.append(j)


def solution(n, computers):
    answer = 0
    visit = [False] * n
    for i in range(0, n):
        if not visit[i]:
            bfs(i, visit, computers, n)
            answer += 1
    return answer
