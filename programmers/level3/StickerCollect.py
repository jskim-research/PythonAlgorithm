"""
programmers 스티커 모으기(2) 풀이

시작 시간: 2022.09.24 19:42, 21:25 => 포기
끝 시간: 2022.09.24 23:57
걸린 시간: 그냥 못 푼거나 마찬가지임
병목 원인: 점화식 자체를 떠올리는데 어려움이 있었음. cycle이 추가되면서 개념의 혼동이 온것으로 보임. 오른쪽의 문제가 왼쪽의 sub-solution으로부터 도출되는 전형적인 DP이고, cycle 처리를 위해 양 끝단을 자르는 선택지가 있음.
          이렇게 양 끝단을 자르면서 두 개의 case가 생기는데 각 case가 서로 독립적으로 최대합을 구할 수 있는 지가 관건.
          실제로 양 끝단 중 하나를 고르면 다른 하나는 고를 수 없기 때문에 독립적이다.
개선 여지:
"""


def get_index(index, n):
    # 실제로 음수 index는 -1 만 생각하지만 따로 예외처리는 안했음
    if index < 0:
        index = n + index  # -1 => n-1
    else:
        index = index % n  # (n-1) + 1 => 0
    return index


def solution(sticker):
    if len(sticker) == 1:
        return sticker[0]

    s = sticker[1:]
    memo1 = [0] * len(s)
    memo1[0] = s[0]

    for i in range(1, len(s)):
        if i == 1:
            memo1[i] = max(s[i], memo1[i - 1])
        else:
            memo1[i] = max(memo1[i - 1], memo1[i - 2] + s[i])

    s = sticker[:-1]
    memo2 = [0] * len(s)
    memo2[0] = s[0]
    for i in range(1, len(s)):
        if i == 1:
            memo2[i] = max(s[i], memo2[i - 1])
        else:
            memo2[i] = max(memo2[i - 1], memo2[i - 2] + s[i])

    return max(memo1[-1], memo2[-1])



