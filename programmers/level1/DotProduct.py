"""
Programmers 내적 풀이

ToDo:
    * typecast better way 알아보기
"""

import numpy as np


def solution(a, b):
    answer = np.dot(np.array(a), np.array(b).T)
    return int(answer)  # typecast가 너무 강력함
