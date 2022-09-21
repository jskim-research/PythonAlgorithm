"""
코딩 문제를 풀이중 유용한 함수들 정리

최대한 가독성, 효율성 을 생각하여 다듬을 예정
"""
import math
from typing import List


def count_digit(number: int):
    """
    숫자 자릿수 반환

    Args:
        number: positive integer (number >= 0)
    Returns:
        0~9 => return 1, 10~99 => return 2, 100~999 => return 3, ...
    """
    return len(str(number))


def rotate_2d_coord(x: float, y: float, theta: float):
    """
    rotate x, y by theta (from right to left)

    Args:
        x: x
        y: y
        theta: degree
    Returns:
        x, y rotated by theta
    """
    theta = math.radians(theta)
    # (cos(a)x + sin(a)y => cos(a+theta)x + sin(a+theta)y 정리해보면 밑과 같이 나옴)
    ret_x = math.cos(theta) * x - math.sin(theta) * y
    ret_y = math.sin(theta) * x + math.cos(theta) * y
    return ret_x, ret_y


def rotate_matrix_90_degree(mat: List[List[float]]):
    """
    rotate matrix by 90 degree

    Args:
        mat: target matrix which has rectangular shape
    Returns:
        rotated matrix by 90 degree
    """
    size = len(mat)
    if size <= 0 or size != len(mat[0]):
        raise ValueError("size should be larger than 0 or "
                         "the matrix should be rectangular which has same width and height")

    ret_mat = [[0] * size for _ in range(size)]
    for i in range(0, size):
        for j in range(0, size):
            ret_mat[j][size-1-i] = mat[i][j]
    return ret_mat


def sum_digit(number: int):
    """
    왼쪽 끝 자릿수부터 오른쪽 끝 자릿수까지 순회

    Args:
        number: 정수
    Returns:
        자릿수들의 합
    """
    if number < 10:
        return number
    return (number % 10) + sum_digit(number // 10)


if __name__ == "__main__":
    mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(rotate_matrix_90_degree(mat))
