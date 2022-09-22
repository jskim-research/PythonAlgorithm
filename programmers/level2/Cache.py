"""
programmers 캐시 풀이

시작 시간: 2022.09.22 14:44
끝 시간: 2022.09.22 15:10
걸린 시간: 26분
병목 원인: 문제 제약 사항 스킵함 + least recently used 라는 method가 새로운 input이 들어왔을 때
         어떻게 반응하는가에 대한 제대로 된 정의를 내리지 않았음
개선 여지:
"""


def solution(cacheSize, cities):
    answer = 0
    cache = {}

    for idx in range(len(cities)):
        cities[idx] = cities[idx].lower()

    for idx, city in enumerate(cities):
        if city in cache:
            answer += 1
            cache[city] = idx
        else:
            answer += 5
            cache[city] = idx
            if len(cache) > cacheSize:
                # 가장 오래된 cache 원소 제거
                oldest_cache_elem = None
                for k, v in cache.items():
                    if oldest_cache_elem is None:
                        oldest_cache_elem = (k, v)
                    else:
                        if v < oldest_cache_elem[1]:
                            oldest_cache_elem = (k, v)
                if oldest_cache_elem is not None:
                    del cache[oldest_cache_elem[0]]

    return answer