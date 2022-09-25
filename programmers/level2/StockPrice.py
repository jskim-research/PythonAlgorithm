"""
programmers 주식가격 풀이

시작 시간: 2022.09.25 08:35
끝 시간: 2022.09.25 09:05
걸린 시간: 30분
병목 원인: 계속 유지되다가 떨어진 경우 유지된 값들을 전부 tracking 해서 떨어진 값 시점 이랑 차이를 구해야하는데 뒤에서부터 접근하므로 stack에 저장해두고 빼내는 형태가 최적
개선 여지:
"""


def solution(prices):
    answer = [0] * len(prices)
    stack = []
    for idx, p in enumerate(prices):
        while stack and stack[-1][1] > p:
            s = stack.pop()
            answer[s[0]] = idx - s[0]
        stack.append((idx, p))

    while stack:
        s = stack.pop()
        answer[s[0]] = len(prices) - 1 - s[0]

    return answer



