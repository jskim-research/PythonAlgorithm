"""
programmers 이중우선순위큐 풀이

시작 시간: 2022.09.21 22:34
끝 시간: 2022.09.21 23:04
걸린 시간: 30분
병목 원인: 깔끔한 코드를 못 짜서 지저분한 코드로 시간 오래 걸림 => 는 동기화 신경쓰게 되면 불가피한 문제인듯
개선 여지:
"""
import heapq as hq
from collections import defaultdict


def solution(operations):
    min_q = []
    min_q_copy_num = defaultdict(int)
    max_q = []
    max_q_copy_num = defaultdict(int)

    for op in operations:
        command, num = op.split()
        num = int(num)
        if command == 'I':
            hq.heappush(min_q, num)
            hq.heappush(max_q, -num)
        elif command == 'D':
            if num == -1:
                while min_q:
                    min_data = hq.heappop(min_q)
                    if min_q_copy_num[min_data] >= 1:
                        min_q_copy_num[min_data] -= 1
                    else:
                        max_q_copy_num[min_data] += 1
                        break
            elif num == 1:
                while max_q:
                    max_data = -hq.heappop(max_q)
                    if max_q_copy_num[max_data] >= 1:
                        max_q_copy_num[max_data] -= 1
                    else:
                        min_q_copy_num[max_data] += 1
                        break

    answer = [0, 0]
    while min_q:
        min_data = hq.heappop(min_q)
        if min_q_copy_num[min_data] >= 1:
            min_q_copy_num[min_data] -= 1
        else:
            answer[1] = min_data
            break

    while max_q:
        max_data = -hq.heappop(max_q)
        if max_q_copy_num[max_data] >= 1:
            max_q_copy_num[max_data] -= 1
        else:
            answer[0] = max_data
            break

    return answer

