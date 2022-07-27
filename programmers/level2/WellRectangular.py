"""
programmers 멀쩡한 사각형 문제풀이

시작 시간: ?
끝 시간: ?
걸린 시간: 타인 풀이 참고
병목 원인:
개선 방법: small case로 확실히 나눌 수 있으면 먼저 small case에 대한 답만 찾기 or 멀쩡하지 않은 사각형 제거하고 중복 제거 부분 보상
"""
import math


def solution(w,h):
    # g = gcd 일 때
    # g == 1 인 case 가 g 개 만큼 존재
    # g == 1 인 small case에 대한 답 (w + h - 1) * g 가 최종 정답
    g = math.gcd(w, h)
    answer = w * h - g * (w // g + h // g - 1)  # small case => bigger case 풀이
    # answer = w * h - w - h + g  # 멀쩡하지 않은 사각형부터 제거하고 중복 제거 보상
    # 수식을 어떻게 구성하냐에 따라 풀이 방식이 많이 다르다. 하나의 식에서도 여러 방식을 떠올릴 수 있을 듯


    return answer