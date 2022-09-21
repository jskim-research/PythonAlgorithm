"""
programmers 다음 큰 숫자  풀이

시작 시간: 2022.09.21 14:58
끝 시간: 2022.09.21 15:48
걸린 시간: 50분
병목 원인: n+1 씩 하면서 brute force 하는 방식이 시간복잡도가 크지않음에도 더 좋은 방식을 찾으려다 망함
        다만 효율성 테스트가 꽤 엄격해서 가장 많은 시간이 걸리는 2의 제곱 부분만 별도 처리가 들어감 
개선 여지:
"""


def get_one_num(n):
    b = str(bin(n))
    return sum([1 for c in b if c == '1'])


def solution(n):
    target_bin_len = get_one_num(n)

    for i in range(1, 21):
        if 2 ** i == n:
            return n * 2

    while True:
        n = n + 1
        if abs(target_bin_len - get_one_num(n)) == 0:
            break
    return n
