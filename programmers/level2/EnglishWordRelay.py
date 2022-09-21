"""
programmers 영어 끝말잇기 풀이

시작 시간: 2022.09.21 16:08
끝 시간: 2022.09.21 16:19
걸린 시간: 11분
병목 원인:
개선 여지:
"""


def solution(n, words):
    s = set([words[0]])

    for i in range(0, len(words) - 1):
        if words[i][-1] != words[i + 1][0] or words[i + 1] in s:
            return [(i + 1) % n + 1, (i + 1) // n + 1]
        s.add(words[i + 1])

    return [0, 0]

