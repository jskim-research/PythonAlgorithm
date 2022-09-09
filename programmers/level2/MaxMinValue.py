"""
programmers 최댓값과 최솟값 문제풀이

시작 시간: 2022.09.09 22:40
끝 시간: 2022.09.09 22:42
걸린 시간: 3분
병목 원인:
개선 방법:
"""
def solution(s):
    values = list(map(int, s.split(" ")))
    answer = f"{min(values)} {max(values)}"

    return answer
