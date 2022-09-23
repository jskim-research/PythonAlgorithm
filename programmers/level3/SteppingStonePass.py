"""
programmers 징검다리 건너기 풀이

시작 시간: 2022.09.23 9:54
끝 시간: 2022.09.23 11:14
걸린 시간: 1시간 20분
병목 원인: 괴상한 binary search 아이디어에 너무 많은 시간을 씀. => 간단한 brute force idea, min(k개씩 묶어서 max 값들) 아이디어에서 출발하면 코드는 지저분해도 풀 수 있음.
개선 여지:
"""
from heapq import heappush, heappop
from collections import deque, defaultdict


def solution(stones, k):
    h = []
    cur_block = stones[:k]
    stones = stones[k:]
    max_list = []
    del_log = defaultdict(int)

    for b in cur_block:
        heappush(h, -b)
    max_list.append(-h[0])
    cur_block = deque(cur_block)

    for s in stones:
        del_log[cur_block[0]] += 1
        cur_block.popleft()
        cur_block.append(s)
        heappush(h, -s)
        while h:
            if del_log[-h[0]] >= 1:
                del_log[-h[0]] -= 1
                heappop(h)
            else:
                break
        max_list.append(-h[0])

    return min(max_list)



