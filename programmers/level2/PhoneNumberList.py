"""
programmers 전화번호 목록 문제풀이

시작 시간: 2022.07.30 12:57
끝 시간: 2022.07.30 13:19
걸린 시간: 22분
병목 원인: sort 하고 풀면 인접한 것만 startswith 체크하면 되긴하는데 hash가 좀 더 빠를 것 같음. O(nk) 과 O(nklogn) 차이니까.
개선 방법:
"""
# 20개
from collections import defaultdict


def solution(phone_book):
    answer = True
    d = defaultdict(int)

    # O(n * k)
    for num in phone_book:
        for i in range(len(num)):
            d[num[:i + 1]] += 1

    for num in phone_book:
        if d[num] > 1:
            answer = False
            break

    return answer

