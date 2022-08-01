"""
programmers 프린터 문제풀이

시작 시간:
끝 시간:
걸린 시간: ?
병목 원인: 아마도, simulation 문제였는데 너무 다른 방법을 찾고 있었음
개선 방법:
"""
from collections import deque


def solution(priorities, location):
    answer = 0
    n = len(priorities)
    q = deque(priorities)
    sort = sorted(priorities)

    while q:
        v = q.popleft()
        if v == sort[-1]:  # 현재 뽑은 것이 가장 중요한 문서임
            sort.pop()
            answer += 1
            n -= 1
            if location == 0:
                break
        else:  # 나머지 인쇄 대기목록에서 더 중요한 문서가 한 개라도 존재
            q.append(v)

        location = n - 1 if location == 0 else location - 1  # n - 1 => 

    return answer
