"""
programmers 로또의 최고 순위와 최저 순위

시작 시간: 2022.07.18 22:32
끝 시간: 2022.07.18 22:47
걸린 시간: 15분
병목 원인: 0의 개수를 세는 거는 list.count(0)으로 되는데 못 썼고, 6/7 위 동일시하는 것을 좀 복잡하게 표현함
개선 여지: len(set1 & set2) 으로 겹치는 것의 개수 + list.count(0)
"""
def solution(lottos, win_nums):
    least = min(6, 7 - sum(1 if lotto in win_nums else 0 for lotto in lottos))
    highest = max(1, least - sum(1 if lotto == 0 else 0 for lotto in lottos))
    answer = [highest, least]

    return answer