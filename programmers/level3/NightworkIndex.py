"""
programmers 야근지수 풀이

시작 시간: 2022.09.14 22:00
끝 시간: 2022.09.14 23:31
걸린 시간: 1시간 31분
병목 원인: 최댓값을 하나씩 뽑는다는 개념으로 접근하면 max heap을 활용할 수 있었음. but, 알고리즘 시간 복잡도는 내가 생각한 것이 더 깔끔했음. 다만 가독성이 너무 안 좋음.
개선 여지:
"""
import heapq


def solution2(n, works):
    hq = []
    answer = sum([work * work for work in works])

    for work in works:
        heapq.heappush(hq, -work)

    if n >= answer:
        return 0

    while n > 0:
        n -= 1
        max_value = -heapq.heappop(hq)
        max_value_reduce = max(max_value - 1, 0)
        answer -= max_value * max_value - max_value_reduce * max_value_reduce
        heapq.heappush(hq, -(max_value_reduce))

    return sum([v * v for v in hq])


def solution1(n, works):
    answer = sum([work * work for work in works])  # maximum
    works = sorted(works, reverse=True)

    if len(works) == 1:
        return max(works[0] - n, 0)

    for k in range(0, len(works) - 1):
        diff = works[k] - works[k + 1]  # 성공 시 0~k+1 까지 그룹 확장
        if diff * (k + 1) > n:
            k -= 1
            break
        else:
            answer -= (k + 1) * (works[k] * works[k] - (works[k] - diff) * (works[k] - diff))
            works[k] = works[k + 1]
            n -= diff * (k + 1)

    group_num = works[k + 1]
    while n > 0:
        divide = max(n // (k + 2), 1)
        group_num_divide = max(group_num - divide, 0)
        for _ in range(0, k + 2):
            reduce = group_num * group_num - group_num_divide * group_num_divide
            answer -= reduce
            n -= divide
            if n <= 0:
                break
        group_num = max(group_num - divide, 0)

    return max(answer, 0)

