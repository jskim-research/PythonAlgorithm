"""
programmers 여행경로 풀이

시작 시간: 2022.09.17 21:25
끝 시간: 2022.09.17 21:50
걸린 시간: 25분
병목 원인: python 식의 dfs, bfs 코드 짜는 방법 봐야할듯.
개선 여지:
"""
from collections import defaultdict


def dfs(cur_city, tickets, visit, path, answer):
    for idx, ticket in enumerate(tickets):
        if ticket[0] == cur_city and not visit[idx]:
            visit[idx] = True
            path.append(idx)
            dfs(ticket[1], tickets, visit, path, answer)
            path.pop()
            visit[idx] = False
    if len(path) == len(tickets):
        answer.append(["ICN"] + [tickets[idx][1] for idx in path])


def solution(tickets):
    visit = defaultdict(bool)
    path = []
    answer = []
    dfs("ICN", tickets, visit, path, answer)
    answer = ["".join(a) for a in answer]
    answer = sorted(answer)[0]
    answer = [answer[idx:idx+3] for idx in range(0, len(answer), 3)]

    return answer