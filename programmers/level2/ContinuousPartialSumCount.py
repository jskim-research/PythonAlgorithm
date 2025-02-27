"""
programmers 2xN 타일링 풀이

시작 시간: 2025.02.28 07:31
끝 시간: 2025.02.28 07:41
걸린 시간: 10분
병목 원인:
개선 여지:
"""


def solution(elements):
    n = len(elements)
    all_sum = set()
    for i in range(n):
        s = elements[i]
        all_sum.add(s)
        for j in range(1, n):
            s += elements[(i + j) % n]
            all_sum.add(s)
    return len(all_sum)