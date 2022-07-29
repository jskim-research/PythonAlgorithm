"""
programmers 타겟넘버 문제풀이

시작 시간: 2022.07.30 6:40
끝 시간: 2022.07.30 6:50
걸린 시간: 10분
병목 원인:
개선 방법:
"""


# def(sum + n_i) + def(sum - n_i) // if last_num and sum == target: return 1 else return 0
def search(numbers, level, sum, target):
    if level == len(numbers):
        if sum == target:
            return 1
        else:
            return 0
    return search(numbers, level + 1, sum + numbers[level], target) + search(numbers, level + 1, sum - numbers[level],
                                                                             target)


def solution(numbers, target):
    answer = search(numbers, 0, 0, target)
    return answer


"""pythonic way from other solution
from itertools import product
def solution(numbers, target):
    l = [(x, -x) for x in numbers]
    s = list(map(sum, product(*l)))
    return s.count(target)
"""
