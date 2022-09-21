"""
programmers 숫자게임 풀이

시작 시간: 2022.09.22 00:36
끝 시간: 2022.09.22 00:48
걸린 시간: 12분
병목 원인:
개선 여지:
"""
from collections import deque


def solution(A, B):
    A = deque(sorted(A, reverse=True))
    B = deque(sorted(B, reverse=True))
    answer = 0

    while A:
        if A[0] >= B[0]:
            # 지는 상황이므로 작은 수를 대신 내기
            B.appendleft(B.pop())
        else:
            # 이기는 상황.. 어차피 서로 최대값이므로 아슬아슬하게 이길 필요없음
            answer += 1

        # 승부난 카드 버리기
        A.popleft()
        B.popleft()

    return answer




