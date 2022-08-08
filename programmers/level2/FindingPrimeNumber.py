"""
programmers 소수찾기 문제풀이

시작 시간: 2022.08.08 22:17
끝 시간: 2022.08.08 23:00
걸린 시간: 43분
병목 원인: 순열 다루는 법에 대해서 잘 몰랐음 + 문제에 대해서 잘 이해 못함
개선 방법: 순열 다루는 법은 배우면 되고, 문제 이해는 test case를 실제로 대입해보고 했어야했음 ===> 무엇보다 순열 안 써도 set에서 없애는 방식도 있더라
"""
# 소수들 전부 저장 (9999999 까지)
# DFS로 numbers에서 하나씩 빼가면서 전부 탐색 (7!)
# found number in 소수들 count ++
from itertools import permutations


def solution(numbers):
    max_num = 10000000
    s = set()
    idx_list = [i for i in range(len(numbers))]
    is_sosu = [True for i in range(max_num)]
    is_sosu[0] = False
    is_sosu[1] = False
    for i in range(2, max_num):
        if is_sosu[i]:
            for j in range(i + i, max_num, i):
                is_sosu[j] = False
    answer = 0

    for i in range(1, len(numbers) + 1):
        p = list(permutations(idx_list, i))
        for idx_perm in p:
            tmp_str = ""
            for idx in idx_perm:
                tmp_str += numbers[idx]
            tmp_int = int(tmp_str)
            if is_sosu[tmp_int] and tmp_int not in s:
                s.add(tmp_int)
                answer += 1

    return answer


def solution2(numbers):
    # 소수들 전부 저장 (9999999 까지)
    # DFS로 numbers에서 하나씩 빼가면서 전부 탐색 (7!)
    # found number in 소수들 count ++
    from itertools import permutations

    def solution(numbers):
        s = set()

        for i in range(len(numbers)):
            s |= set(map(int, map("".join, permutations(list(numbers), i + 1))))

        s -= set([0, 1])  # 0, 1 should be counted as sosu

        max_s = max(s)
        for i in range(2, max_s + 1):
            s -= set([j for j in range(2 * i, max_s + 1, i)])

        answer = len(s)
        return answer