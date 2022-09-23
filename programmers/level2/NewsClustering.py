"""
programmers 뉴스 클러스터링 풀이

시작 시간: 2022.09.23 16:04
끝 시간: 2022.09.23 16:24
걸린 시간: 20분
병목 원인:
개선 여지:
"""
from collections import defaultdict


def solution(str1, str2):
    m1 = defaultdict(int)
    m2 = defaultdict(int)
    str1 = str1.lower()
    str2 = str2.lower()
    s1 = set()
    s2 = set()

    for i in range(len(str1) - 1):
        s = str1[i:i + 2]
        if not ('a' <= s[0] <= 'z' and 'a' <= s[1] <= 'z'):
            continue
        s1.add(s)
        m1[s] += 1

    for i in range(len(str2) - 1):
        s = str2[i:i + 2]
        if not ('a' <= s[0] <= 'z' and 'a' <= s[1] <= 'z'):
            continue
        s2.add(s)
        m2[s] += 1

    cross = s1 & s2
    total = s1 | s2

    cross_sum = sum([min(m1[v], m2[v]) for v in cross])
    total_sum = sum([max(m1[v], m2[v]) for v in total])

    if total_sum == 0:
        return 65536
    else:
        return int((cross_sum / total_sum) * 65536)



