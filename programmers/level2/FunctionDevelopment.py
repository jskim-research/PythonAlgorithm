"""
programmers 기능개발 문제풀이

시작 시간: 2022.07.27 22:03
끝 시간: 2022.07.27 22:11
걸린 시간: 8 분
병목 원인:
개선 방법:
"""
import math


def solution(progresses, speeds):
    remain_day = list(map(lambda x: math.ceil((100 - x[0]) / x[1]), zip(progresses, speeds)))
    first_task_days = remain_day[0]
    answer = [0]

    # 앞의 작업일수보다 작은 애들은 전부 같이 배포됨
    for day in remain_day:
        if day <= first_task_days:
            answer[-1] += 1
        else:
            first_task_days = day
            answer.append(1)
    return answer
