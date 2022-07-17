"""
programmers k번째 수 풀이

시작 시간: 2022.07.17 18:15
끝 시간: 2022.07.17 18:19
걸린 시간: 4분
병목 원인:
개선 여지: map 함수로 한번에 처리할 수 있었는데 반복문 까지 넣어서 처리함
"""
def solution(array, commands):
    answer = []
    for command in commands:
        i, j, k = command
        answer.append(sorted(array[i - 1:j])[k - 1])

    return answer
