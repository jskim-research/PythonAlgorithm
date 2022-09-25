"""
programmers 주차요금계산 풀이

시작 시간: 2022.09.23 22:04
끝 시간: 2022.09.23 22:19
걸린 시간: 15분
병목 원인:
개선 여지:
"""
import math
from collections import defaultdict


def solution(fees, records):
    m = defaultdict(list)
    answer = []
    for r in records:
        r = r.split()
        t = int(r[0][:2]) * 60 + int(r[0][3:])
        m[r[1]].append(t)

    for k, v in m.items():
        if len(v) % 2 != 0:
            v.append(23 * 60 + 59)
        parking_t = sum([v[i + 1] - v[i] for i in range(0, len(v), 2)])
        parking_rate = fees[1] if parking_t <= fees[0] else fees[1] + math.ceil((parking_t - fees[0]) / fees[2]) * fees[
            3]
        answer.append((k, parking_rate))

    answer = [v[1] for v in sorted(answer, key=lambda x: x[0])]
    return answer





