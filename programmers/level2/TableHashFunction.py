"""
programmers 테이블 해시 함수 풀이

시작 시간: 2025.03.02 11:30
끝 시간: 2025.03.02 11:46
걸린 시간: 16분
병목 원인:
개선 여지: 
"""


def solution(data, col, row_begin, row_end):
    # col - 1 번째 값 기준 오름차순
    # 만약 같을 경우 첫 번째 값 기준 내림차순
    data = sorted(data, key=lambda x: (x[col - 1], -x[0]))
    answer = None
    s_list = []

    for i in range(row_begin - 1, row_end):
        s_i = 0
        for j in range(len(data[i])):
            s_i += data[i][j] % (i + 1)

        if answer is None:
            answer = s_i
        else:
            answer = s_i ^ answer

    return answer
