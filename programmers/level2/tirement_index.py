"""
programmers 피로도 풀이

시작 시간: 2022.10.07 20:05
끝 시간: 2022.10.07 20:26
걸린 시간: 21분
병목 원인: 완전탐색 문제에서 경우들을 어떻게 셀 것인가 이해없이 들어감
개선 여지: 완전탐색 문제에서는 해당 문제가 어떠한 경우의 수를 갖는지 파악해야만 코드를 짤 때 잘 짤 수 있다.
"""


def get_max_count(dungeons, k):
    max_cnt = 0

    for i, v in enumerate(dungeons):
        if v[0] <= k:
            max_cnt = max(max_cnt, get_max_count(dungeons[:i] + dungeons[i + 1:], k - v[1]) + 1)

    return max_cnt


def solution(k, dungeons):
    return get_max_count(dungeons, k)



