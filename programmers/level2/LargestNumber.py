"""
programmers 가장 큰 수 문제풀이

시작 시간: 2022.08.10 22:48
끝 시간: 2022.08.10 23:44
걸린 시간: 54분 + 답지 참고
병목 원인: 하나의 solution에 매몰되어 해당 solution이 문제를 더욱 어렵게 만드는 것을 해결할 방법을 강구하지 못했음
개선 방법:
"""

"""
1, 10, 100, 1000 에서 뒷자리를 반복시키면 전부 1000, 1000, 1000, 1000이 되어 구분이 힘듬

length가 앞일수록 더 큰 값이라는 것이 보장되어야 함 => 밑 방법이 아니어도 상관없지만 이 기능만 달성하면 됨

10 10
100 1
1000
"""


def transform(x: str):
    if len(x) == 1:
        x += x * 3
    elif len(x) == 2:
        x += x
    elif len(x) == 3:
        x += x[0]
    return x


def solution(numbers):
    answer = ''

    if max(numbers) == 0:
        return "0"

    numbers = list(map(str, numbers))
    sorted_numbers = sorted(numbers, key=transform, reverse=True)
    answer = "".join(sorted_numbers)
    return answer