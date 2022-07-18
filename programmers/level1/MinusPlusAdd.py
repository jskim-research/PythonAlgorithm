"""
programmers 음양더하기

시작 시간: 2022.07.18 22:24
끝 시간: 2022.07.18 22:28
걸린 시간: 4분
병목 원인: pythonic way를 찾다보니 그렇게 됨
개선 여지: return sum(absolute if sign else -absolute for absolute, sign in zip(absolutes, signs))
"""
def solution(absolutes, signs):
    answer = 0
    for i, sign in enumerate(signs):
        answer += absolutes[i] if sign else -absolutes[i]
    return answer