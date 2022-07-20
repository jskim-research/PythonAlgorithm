"""
programmers 폰켓몬 문제풀이

시작 시간: 2022.07.20 21:59
끝 시간: 2022.07.20 22:03
걸린 시간: 4분
병목 원인: x
개선 방법:
"""
def solution(nums):
    answer = min(len(set(nums)), len(nums)//2)
    return answer

