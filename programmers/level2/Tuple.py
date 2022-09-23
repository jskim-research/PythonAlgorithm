"""
programmers 튜플 풀이

시작 시간: 2022.09.23 15:28
끝 시간: 2022.09.23 15:47
걸린 시간: 19분
병목 원인: 정규식을 제대로 활용하지 못해서 처음에 파싱 부분에서 오래 걸림.
개선 여지:
"""


def solution(s):
    answer = []

    s = s[1:-1]
    vals = []
    start = 0
    for idx, v in enumerate(s):
        if v == '{':
            start = idx
        elif v == '}':
            end = idx
            vals.append(s[start + 1:end])

    vals = sorted([v.split(',') for v in vals], key=lambda x: len(x))
    v_set = set()

    for val in vals:
        for v in val:
            if v not in v_set:
                v_set.add(v)
                answer.append(v)
    return list(map(int, answer))



