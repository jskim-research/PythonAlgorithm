"""
programmers 행렬 테두리 회전 문제풀이

시작 시간: 2022.08.11 18:46
끝 시간: 2022.08.11 ?
걸린 시간: 2시간 이상
병목 원인: list slicing 보다 넘파이를 빨리 사용했어야할듯
개선 방법:
"""

import numpy as np


def rotate(matrix, query):
    y1, x1, y2, x2 = query
    x1, y1, x2, y2 = x1 - 1, y1 - 1, x2 - 1, y2 - 1

    matrix = np.array(matrix)
    cpy_matrix = np.copy(matrix)
    min_val = 100000

    cpy_matrix[y1, x1 + 1: x2 + 1] = matrix[y1, x1: x2]
    min_val = min(min_val, matrix[y1, x1: x2].min())

    cpy_matrix[y1 + 1: y2 + 1, x2] = matrix[y1: y2, x2]
    min_val = min(min_val, matrix[y1: y2, x2].min())

    cpy_matrix[y2, x1:x2] = matrix[y2, x1 + 1: x2 + 1]
    min_val = min(min_val, matrix[y2, x1 + 1: x2 + 1].min())

    cpy_matrix[y1:y2, x1] = matrix[y1 + 1: y2 + 1, x1]
    min_val = min(min_val, matrix[y1 + 1: y2 + 1, x1].min())

    print(cpy_matrix)
    return min_val


def solution(rows, columns, queries):
    answer = []
    matrix = [[r * columns + c + 1 for c in range(columns)] for r in range(rows)]
    for q in queries:
        answer.append(rotate(matrix, q))
    return answer


print(solution(100, 97, [[1, 1, 100, 97]]))

