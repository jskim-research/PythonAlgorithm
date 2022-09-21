"""
programmers 베스트앨범 풀이

시작 시간: 2022.09.21 23:51
끝 시간: 2022.09.21 00:08
걸린 시간: 17분
병목 원인:
개선 여지:
"""
from collections import defaultdict


def solution(genres, plays):
    answer = []
    data = defaultdict(list)

    for idx, p in enumerate(plays):
        data[genres[idx]].append((p, idx))

    best_genre = []
    for key, value in data.items():
        data[key] = sorted(data[key], key=lambda x: x[0], reverse=True)
        best_genre.append((key, sum(map(lambda x: x[0], value))))

    best_genre = sorted(best_genre, key=lambda x: x[1], reverse=True)

    for g in best_genre:
        g = g[0]
        for i in range(0, min(len(data[g]), 2)):
            answer.append(data[g][i][1])

    return answer
