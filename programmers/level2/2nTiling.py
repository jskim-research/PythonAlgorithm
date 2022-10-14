"""
programmers 2xN 타일링 풀이

시작 시간: 2022.10.14 11:51
끝 시간: 2022.10.14 11:59
걸린 시간: 8분
병목 원인:
개선 여지:
"""


def solution(n):
    tile_cases = [0] * (n + 2)
    tile_cases[n] = 1

    for i in range(n - 1, -1, -1):
        tile_cases[i] = (tile_cases[i + 1] + tile_cases[i + 2]) % 1000000007

    return tile_cases[0]



