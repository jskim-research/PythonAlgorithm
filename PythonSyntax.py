"""
간단한 python 문법 코드 정리
"""
# list comprehension
a = [i for i in range(20) if i % 2 == 1]  # 1차원 배열
b = [[0 for i in range(4)] for j in range(5)]  # 2차원 배열

# list method
# append
# sort(reverse=False)
# reverse
# insert(삽일할 위치 인덱스, 삽입할 값)
# count(특정값)
# remove(특정값) => 여러 개의 값 존재 시 하나만 제거

# tuple
# 값을 바꿀 수 없어서 바꾸면 안되는 상황에 자주 사용됨

# dictionary
# keys, values 함수 존재

# set
# 중복 허용 x, 순서 없음
# 존재 검사 연산 O(1)
# set 간 합집합 |, 교집합 &, 차집합 -
# remove(특정값), add(특정값), update([특정값1, 특정값2, ...]) / remove, add O(1)

# lambda
print((lambda _a, _b: _a + _b)(5, 8))

# 입출력
# input() 보다 더 빠르게 입력을 받아들일 수 있는 함수
import sys
# data = sys.stdin.readline().rstrip()  # 한 줄 읽고 줄바꿈 제거
# print(data)

# 주요 라이브러리
# 내장 함수 (print, input, sorted 등)
result = sorted([('홍길동', 35), ('이순신', 75), ('아무개', 50)], key=lambda x: x[1], reverse=False)  # sort 기준 설정 가능
print(result)
result = [('홍길동', 35), ('이순신', 75), ('아무개', 50)]
result.sort(key=lambda x: x[1])
print(result)

# itertools: 반복되는 형태 데이터 처리 기능 제공, 조합과 순열 제공
from itertools import permutations, combinations, product, combinations_with_replacement

data = ['A', 'B', 'C']
print(list(permutations(data, 3)))
print(list(combinations(data, 2)))
print(list(product(data, repeat=2)))  # 순서 고려 x, 원소를 중복하여 뽑는다
print(list(combinations_with_replacement(data, 2)))  # 순서 고려, 원소를 중복하여 뽑는다

# heapq: heap 기능 제공 (우선 순위 큐 기능 구현을 위해 사용)
import heapq


def heapsort(iterable):
    h = []
    result = []
    for value in iterable:
        heapq.heappush(h, value)  # min-heap
    for _ in range(len(h)):
        result.append(heapq.heappop(h))
    return result

data = [1, 5, 3, 2, 7, 8, 3]
print(heapsort(data))

# bisect: 이진 탐색 기능 제공
from bisect import bisect_left, bisect_right
data = [1, 5, 7, 9, 10, 11, 16, 16, 17, 19, 20]
print(bisect_left(data, 16))  # 값이 특정 범위에 속하는 개수 (왼쪽 기준)
print(bisect_right(data, 20))  # 값이 특정 범위에 속하는 개수 (오른쪽 기준)
# left_value <= x <= right_value 개수
print(bisect_right(data, 20) - bisect_left(data, 16))

# collections: deque, Counter 등 유용한 자료구조 포함
from collections import deque, Counter

# deque => 앞 뒤 삽입, 삭제 O(1)으로 queue로 사용하기 적합
data = deque([2, 3, 4])
data.appendleft(1)
data.append(5)
print(data)
print(data.pop())
print(data.popleft())

# 값 등장 횟수 반환
counter = Counter(['red', 'blue', 'red', 'green', 'blue'])
print(counter['red'])
print(counter['blue'])
print(counter['green'])

# math: PI, 최대공약수(GCD), 삼각함수 등등 유용한 수학적 기능 제공
import math

print(math.factorial(5))
print(math.gcd(21, 14))

