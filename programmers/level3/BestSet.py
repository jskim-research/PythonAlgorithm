"""
programmers 최고의집합 풀이

시작 시간: 2022.09.21 23:12
끝 시간: 2022.09.21 23:22
걸린 시간: 10분
병목 원인:
개선 여지: 평균들로 맞추고 for 문 돌려서 +1 을 했는데 그게 아니라 평균+1 의 개수와 평균의 개수만으로 list 생성하면 됨
"""


def solution(n, s):
    if s < n:
        return [-1]
    answer = [s//n for i in range(n)]
    remain = s % n
    for i in range(n):
        if remain <= 0:
            break
        answer[i] += 1
        remain -= 1
    return sorted(answer)
