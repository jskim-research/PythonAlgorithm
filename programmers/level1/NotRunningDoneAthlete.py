"""
programmers 완주하지 못한 선수 풀이

시작 시간: 2022.07.24 11:48
끝 시간: 2022.07.24 11:50
걸린 시간: 2분
병목 원인:
개선 여지:
"""

from collections import defaultdict


def solution(participant, completion):
    p_dict = defaultdict(int)
    c_dict = defaultdict(int)

    for p in participant:
        p_dict[p] += 1

    for c in completion:
        c_dict[c] += 1

    for name in p_dict:
        if c_dict[name] != p_dict[name]:
            answer = name
    return answer
