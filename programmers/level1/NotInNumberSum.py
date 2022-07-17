"""
programmers 없는 숫자 더하기 풀이
"""

import numpy as np

def solution(numbers):
    answer = int(np.sum(np.arange(0, 10)) - np.sum(numbers, dtype=np.int32))
    return answer
