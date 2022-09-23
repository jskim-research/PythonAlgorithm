"""
programmers n^2 배열 자르기 풀이

시작 시간: 2022.09.23 15:53
끝 시간: 2022.09.23 16:02
걸린 시간: 9분
병목 원인:
개선 여지:
"""


def solution(n, left, right):
    answer = []

    for cur in range(left, right + 1):
        i = cur // n
        j = cur % n
        if i == j:
            answer.append(i + 1)
        else:
            answer.append(max(i, j) + 1)

    return answer

