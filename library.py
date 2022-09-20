"""
코딩 문제를 풀이중 유용한 함수들 정리

최대한 가독성, 효율성 을 생각하여 다듬을 예정
"""


def count_digit(number: int):
    """
    숫자 자릿수 반환

    Args:
        number: positive integer (number >= 0)
    Returns:
        0~9 => return 1, 10~99 => return 2, 100~999 => return 3, ...
    """
    return len(str(number))
