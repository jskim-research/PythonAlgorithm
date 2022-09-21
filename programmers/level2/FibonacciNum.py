"""
programmers 피보나치숫자  풀이

시작 시간: 2022.09.21 14:53
끝 시간: 2022.09.21 14:55
걸린 시간: 2분
병목 원인:
개선 여지: 메모리를 적게 할당하기 위해 fib_1, fib_2 두 개의 변수만 두고 푸는 방식을 쓸 수 있다.
"""


def solution(n):
    fib = [0, 1]
    for i in range(2, n+1):
        fib.append(fib[i-1] + fib[i-2])
    return fib[-1] % 1234567

