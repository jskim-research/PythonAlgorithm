"""
programmers 3xN 타일링 풀이

시작 시간: 2025.02.27 10:46
끝 시간: 2025.02.27 11:08
걸린 시간: 22분
병목 원인: 경우의 수 분리를 처음에 제대로 못했음.
개선 여지: 
    문제의 경우를 분해하는 경우 다른 경우가 생길 수 없는 지 조금 더 주의깊게 확인 필요
    또한 점화식의 경우 식 정리가 가능한지 확인
"""


def first_solution(n):
    DIV = 1000000007
    arr = [1, 0, 3]

    for i in range(3, n + 1):
        arr.append((3 * arr[i - 2]))
        for j in range(4, i + 1, 2):
            arr[-1] += 2 * arr[i - j]
        arr[-1] %= DIV
    return arr[-1]


def solution(n):
    # 홀수인 경우 못 채움
    if n % 2 != 0:
        return 0

    # f(n) = 3 * f(n-2) + 2 * (f(n-4) + ... + f(0))
    # f(n-2) = 3 * f(n-4) + 2 * (f(n-6) + ... + f(0))
    # f(n) - f(n-2) = 3 * f(n-2) - f(n-4)
    # f(n) = 4 * f(n-2) - f(n-4) 로 정리됨
    DIV = 1000000007

    fn_2 = 1
    fn_4 = 1

    for _ in range(n // 2):
        fn_2, fn_4 = (4 * fn_2 - fn_4) % DIV, fn_2

    return fn_2

