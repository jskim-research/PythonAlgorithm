"""
programmers 기지국 설치 풀이

시작 시간: 2022.09.22 23:29
끝 시간: 2022.09.22 23:48
걸린 시간: 19분
병목 원인:
개선 여지:
"""


def solution(n, stations, w):
    coverage = [(0, 0)] + [(max(station - w, 1), min(station + w, n)) for station in stations] + [(n + 1, n + 1)]
    gaps = []
    for i in range(1, len(coverage)):
        gap = coverage[i][0] - coverage[i - 1][1] - 1
        if gap > 0:
            gaps.append(gap)
    print(gaps)

    return sum([(gap - 1) // (2 * w + 1) + 1 for gap in gaps])

