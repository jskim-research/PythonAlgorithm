"""
programmers 더 맵게 문제풀이

시작 시간: 2022.07.27 22:19
끝 시간: 2022.07.27 22:30
걸린 시간: 11 분
병목 원인:
개선 방법:
"""
# O(N * log N) 필요
import heapq


def solution(scoville, K):
    answer = 0
    hq = sorted(scoville)
    while len(hq) > 1 and hq[0] < K:
        first_min = heapq.heappop(hq)
        second_min = heapq.heappop(hq)
        heapq.heappush(hq, first_min + 2 * second_min)
        answer += 1

    if (len(hq) == 1 and hq[0] < K) or len(hq) == 0:
        answer = -1
    return answer
