"""
programmers h-index 풀이

시작 시간: 2022.09.22 15:51
끝 시간: 2022.09.22 15:59
걸린 시간: 8분
병목 원인:
개선 여지:
"""
from bisect import bisect_left


# 닭 잡는데 소 잡는 칼 씀;
def solution(citations):
    answer = 0

    size = len(citations)
    citations = sorted(citations)
    for h in range(1, citations[-1]):
        if (size - bisect_left(citations, h)) >= h:
            answer = h
    return answer


def solution2(citations):
    answer = 0
    citations = sorted(citations)
    num_papers = list(reversed(range(1, len(citations) + 1)))
    print(num_papers)

    for c, n in zip(citations, num_papers):
        if n <= c:
            return n  # n 이상의 영향도를 가진 논문이 n 편 있다.
    return 0

