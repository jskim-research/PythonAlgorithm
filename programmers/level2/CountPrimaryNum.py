"""
programmers k진수에서 소수 개수 구하기 풀이

시작 시간: 2022.09.23 16:28
끝 시간: 2022.09.23 17:55
걸린 시간:
병목 원인: 소수 구하기를 잘못 구해서 문제를 굉장히 우회해서 풀었음. 아이디어 자체는 빨리나옴.
개선 여지:
"""
import math
from collections import defaultdict


def k_to_n(n, k):
    if not n:
        return 0
    return int(n[0]) * (k ** (len(n) - 1)) + k_to_n(n[1:], k)


def n_to_k(n, k):
    if n == 0:
        return ''
    return n_to_k(n // k, k) + str(n % k)


def is_prime(n):
    if n == 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def solution(n, k):
    k_num = n_to_k(n, k) + '0'
    nums = []
    is_primary = defaultdict(lambda: True)

    start = 0
    for idx, v in enumerate(k_num):
        if v == '0':
            if k_num[idx - 1] != '0':
                nums.append(k_num[start:idx])
            start = idx + 1


    # 에라토스테네스의 체는 끝 부분이 결정되어야 하는데
    # 끝 부분을 선택하는 과정이 애매함

    max_len = max(map(len, nums))

    # max_num = math.ceil(int(str(k-1)*max_len) ** (1/2))
    max_num = math.ceil((10 ** 13) ** (0.5))

    # is_primary[1] = False
    # for i in range(2, (max_num + 1)):
    #     if is_primary[i]:
    #         j = i
    #         while j+i <= (max_num):
    #             j += i
    #             is_primary[j] = False

    print(nums)
    for num in nums:
        print(num, is_prime(int(num)))

    return sum([1 for v in nums if is_prime(int(v))])