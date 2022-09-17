"""
programmers 단어변환 풀이

시작 시간: 2022.09.17 19:54
끝 시간: 2022.09.17 20:48
걸린 시간: 54분
병목 원인: DFS, BFS 미숙 => tree 최단거리는 BFS임
개선 여지:
"""
from collections import defaultdict

IMPOSSIBLE = 51


def dfs(cur_word, target, dic, visit, words, step):
    if cur_word == target:
        dic[cur_word] = step
        return dic[cur_word]
    dist = IMPOSSIBLE

    for word in words:
        count = sum([1 if c != w else 0 for c, w in zip(cur_word, word)])
        if count == 1 and not visit[word]:
            visit[word] = True
            dist = min(dfs(word, target, dic, visit, words, step + 1), dist)
            visit[word] = False

    if dic[cur_word] != 0:
        #  더 좋은 기록만 기록
        dic[cur_word] = min(dic[cur_word], dist)
    else:
        dic[cur_word] = dist

    return dist


def solution(begin, target, words):
    dic = defaultdict(int)
    visit = defaultdict(bool)
    dfs(begin, target, dic, visit, words, 0)
    answer = 0 if dic[target] == IMPOSSIBLE else dic[target]
    return answer


from collections import deque


def solution2(begin, target, words):
    dist = {begin: 0}
    q = deque([begin])

    while q:
        cur = q.popleft()
        for word in words:
            count = sum([1 if c != w else 0 for c, w in zip(cur, word)])
            if count == 1 and word not in dist:
                q.append(word)
                dist[word] = dist[cur] + 1

    return dist.get(target, 0)