"""
programmers 예상대진표 풀이

시작 시간: 2022.09.22 13:16
끝 시간: 2022.09.22 13:27
걸린 시간: 11분
병목 원인: 종료 조건에 대한 !!검증!!이 없었음.
개선 여지:
"""


def solution(n,a,b):
    answer = 1
    while (a+1)//2 != (b+1)//2:
        a = (a+1) // 2
        b = (b+1) // 2
        answer += 1

    return answer


