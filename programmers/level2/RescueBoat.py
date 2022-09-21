"""
programmers 구명보트 풀이

시작 시간: 2022.09.21 17:21
끝 시간: 2022.09.21 17:39
걸린 시간: 18분
병목 원인:
개선 여지:
"""

from collections import deque


def solution(people, limit):
    q = deque(sorted(people))
    boat = 0

    while q:
        cur_weight = 0
        while q:

            if q:

                max_val = q.pop()
                if cur_weight + max_val <= limit:
                    cur_weight += max_val
                else:
                    q.append(max_val)
                    break

            if q:
                min_val = q.popleft()
                if cur_weight + min_val <= limit:
                    cur_weight += min_val
                else:
                    q.appendleft(min_val)
                    break
        boat += 1
    return boat


# 실제로 맞는 답
# 최대 2명만 탈 수 있음
# 2명 제한이 아니었으면 무거운 놈부터 태운 게 맞겠지만 이 제한으로 인해 가장 큰 값, 가장 작은 값만 보면 되는 단순한 문제가 됨
def solution2(people, limit):
    boat = 0
    first = 0
    last = len(people) - 1
    people = sorted(people)
    while first < last:
        if people[first] + people[last] <= limit:
            first += 1
            last -= 1
        else:  # 안되면 무거운 놈부터 태운다
            last -= 1
        boat += 1
    return boat + 1 if first == last else boat

