"""
코딩 문제를 풀이중 유용한 함수들 정리

최대한 가독성, 효율성 을 생각하여 다듬을 예정
"""
import math


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


