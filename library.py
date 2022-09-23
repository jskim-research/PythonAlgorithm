"""
코딩 문제를 풀이중 유용한 함수들 정리

최대한 가독성, 효율성 을 생각하여 다듬을 예정
"""
import math
from typing import List
from bisect import bisect_left, bisect_right


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


def get_gcd(n1: int, n2: int):
    """두 정수간 최대공약수 (greatest common divisor) 구하기"""
    min_val = min(n1, n2)
    max_divisor = 1
    for i in range(2, min_val+1):
        if n1 % i == 0 and n2 % i == 0:
            max_divisor = i
    return max_divisor


def get_lcm(n1: int, n2: int):
    """두 정수간 최소공배수 (least common multiple) 구하기"""
    gcd = get_gcd(n1, n2)
    lcm = n1 // gcd * n2 // gcd * gcd
    return lcm


def find_below_above(array: List[int], num: int):
    """
    find numbers right above & below num

    Args:
        array:
        num: target number
    Returns:
        [below, above]
    """
    # bisect_left(array, number): 만약 number를 array에 넣는다고 했을 때 들어가야하는 index 중 최소
    # bisect_right : index 중 최대
    left_idx = bisect_left(array, num)
    right_idx = bisect_right(array, num)
    if len(array) == 0:
        print("no data")

    ret = [None, None]
    ret[0] = array[left_idx-1] if left_idx > 0 else None
    ret[1] = array[right_idx] if right_idx < len(array) else None
    return ret


def is_prime(n: int):
    """n이 소수인지 판별"""
    if n < 1:
        raise ValueError("n should be 1 or larger")
    if n == 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        # 제곱근 이하의 값들만 의미가 있다...? => 시간복잡도에 중요한 가정
        if n % i == 0:
            return False
    return True


if __name__ == "__main__":
    mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    # print(rotate_matrix_90_degree(mat))

    print(get_gcd(20, 14))
    print(get_gcd(20, 15))
    print(get_lcm(20, 15))
    print(get_lcm(20, 13))

    data = [1, 4, 6, 8, 9, 13, 17, 21, 23, 25, 27, 28, 33, 40]
    print(find_below_above(data, 2))
    for i in range(-1, 41):
        print(f"{i}: {find_below_above(data, i)}")
