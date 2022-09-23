"""
programmers 보석쇼핑 풀이

시작 시간: 2022.09.23 9:33
끝 시간: 2022.09.23 9:51
걸린 시간: 18분
병목 원인:
개선 여지:
"""
from collections import deque, defaultdict


def solution(gems):
    q = deque()
    s = set()
    m = defaultdict(int)
    cat_num = len(set(gems))
    min_len = 100001

    for idx, g in enumerate(gems):
        q.append((g, idx))
        s.add(g)
        m[g] += 1
        while q:
            if m[q[0][0]] >= 2:
                m[q[0][0]] -= 1
                q.popleft()
            else:
                break
        if len(s) == cat_num and len(q) < min_len:
            min_len = len(q)
            answer = [q[0][1] + 1, q[-1][1] + 1]

    return answer


