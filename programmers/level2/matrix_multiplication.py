"""
programmers 행렬의곱셈 풀이

시작 시간: 2022.09.22 15:31
끝 시간: 2022.09.22 15:50
걸린 시간: 19분
병목 원인: 쉬운 문제인데 size 계산을 잘못함;;
개선 여지:
"""


def solution(arr1, arr2):
    size1, size2 = len(arr1), len(arr2[0])
    mid_size = len(arr1[0])
    answer = [[0] * size2 for _ in range(size1)]

    print(size1, size2, mid_size)

    for i in range(size1):
        for j in range(size2):
            for k in range(mid_size):
                answer[i][j] += arr1[i][k] * arr2[k][j]

    return answer