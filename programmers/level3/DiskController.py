"""
programmers 디스크 컨트롤러 풀이

시작 시간: 2022.09.24 18:07
끝 시간: 2022.09.24 18: 19:03
걸린 시간: 56분
병목 원인: 처음 아이디어를 생각할 때 문제의 답 형태로 내는 것까지의 생각을 안한 것 + 문제 조건 등을 제대로 안 읽은 것 + heap을 사용한 방식을 너무 고집함
개선 여지:
"""
from collections import deque
from heapq import heappush, heappop, heapify


def solution(jobs):
    answer = 0

    jobs = sorted(jobs, key=lambda x: x[0])
    size = len(jobs)
    last_time = jobs[0][0]
    jobs = deque(jobs)

    while jobs:
        candidate = []

        while jobs and jobs[0][0] <= last_time:
            candidate.append(jobs.popleft())

        if candidate:
            min_val = min([c[1] for c in candidate])

            for idx, val in enumerate(candidate):
                if val[1] == min_val:
                    break

            jobs = candidate[:idx] + candidate[idx + 1:] + list(jobs)
            jobs = deque(jobs)
            last_time = last_time + candidate[idx][1]
            answer += last_time - candidate[idx][0]
        else:
            if jobs:
                last_time = jobs[0][0]

    return answer // size


# candidate 집합을 heap 구조에서 계속해서 늘려나가는 형태를 취함
# 시작시간, duration 순으로 정렬하여 후보군은 가장 처음에서만 계속 뽑는 형태가 됨
# 만약 멀리 떨어진 task가 들어오는 경우 simulation 상 현재 시간을 그 task에 맞춰 max 값으로 넣어줌. (항상 겹친다는 가정이면 cur_time += duration 이 맞지만 겹치지 않으면 문제)
def solution2(jobs):
    answer = 0
    cur_time = 0
    jobs = deque(
        sorted([(j[1], j[0]) for j in jobs], key=lambda x: (x[1], x[0])))  # 시작시간순, duration 순 => 항상 앞에서 시작함을 보장
    size = len(jobs)
    candidate = [jobs.popleft()]  # 후보군 보관

    print(jobs)

    while candidate:
        duration, start_time = heappop(candidate)
        cur_time = max(cur_time + duration, duration + start_time)  # current time과 다음 job이 멀리 떨어진 경우 고려
        answer += cur_time - start_time
        while jobs and jobs[0][1] <= cur_time:
            heappush(candidate, jobs.popleft())
        # current time과 다음 job이 떨어져 있는 경우
        # 즉, 후보군으로 못 뽑아서 후보군은 없는데 job은 남아있는 경우가 됨
        if not candidate and jobs:
            heappush(candidate, jobs.popleft())

    return answer // size