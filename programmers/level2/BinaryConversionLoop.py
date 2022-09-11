"""
programmers 이진 변환 반복하기 풀이

시작 시간: 2022.09.11 22:42
끝 시간: 2022.09.11 22:56
걸린 시간: 14분
병목 원인: Counter, count 함수와 bin 함수를 적극적으로 활용하지 않고 직접 구현함
개선 여지:
"""


def count_ones(s):
    return sum([1 for c in s if c == "1"])


def convert_to_binary(i):
    ret = ""
    while i >= 1:
        ret += "1" if i % 2 != 0 else "0"
        i = i // 2
    return "".join(reversed(ret))


def solution(s):
    answer = [0, 0]
    while s != "1":
        ones_num = count_ones(s)
        zeros_num = len(s) - ones_num
        s = convert_to_binary(count_ones(s))
        answer[0] += 1
        answer[1] += zeros_num

    return answer


def solution2(s):
    answer = [0, 0]

    while s != "1":
        ones_num = s.count("1")
        zeros_num = len(s) - ones_num
        s = bin(ones_num)[2:]
        answer[0] += 1
        answer[1] += zeros_num

    return answer


