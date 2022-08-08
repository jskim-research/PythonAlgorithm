"""
programmers 게임 맵 최단거리 문제풀이

시작 시간: 2022.08.02 20:13
끝 시간: 2022.08.02 20:33
걸린 시간: 20분
병목 원인: python 으로 BFS 풀어보는 건 처음이라 조금 시간 걸림
개선 방법:
"""
from collections import deque


def solution(maps):
    n, m = len(maps), len(maps[0])
    visit = [[0 for _ in range(m)] for _ in range(n)]
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    q = deque([(0, 0, 1)])  # row, col, tile # from start point
    visit[0][0] = 1
    answer = -1

    while q:
        p = q.popleft()
        if p[0] == n - 1 and p[1] == m - 1:
            answer = p[2]
            break

        for direction in range(4):
            ny = p[0] + dy[direction]
            nx = p[1] + dx[direction]
            if nx < 0 or nx >= m or ny < 0 or ny >= n:  # 이상 좌표
                continue
            if visit[ny][nx] == 1:  # 이미 방문한 경우
                continue
            if maps[ny][nx] == 0:  # 벽으로 막힌 경우
                continue
            visit[ny][nx] = 1
            q.append((ny, nx, p[2] + 1))

    return answer

