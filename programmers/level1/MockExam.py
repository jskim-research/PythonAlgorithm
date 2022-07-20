"""
programmers 모의고사 문제풀이

시작 시간: 2022.07.20 22:04
끝 시간: 2022.07.20 22:13
걸린 시간: 9분
병목 원인: 깔끔하게 짜는 방법에 대한 고민
개선 방법: 접근 방법은 깔끔했는데 pattern1, 2, 3 처럼 변수로 나누지 말고 list로 구성한 후에 반복문 돌리는 것이 깔끔함
          + comprehension을 쓰면 미리 생성해야하는 list 구문이 줄어듬
"""
def solution(answers):
    # 1 2 3 4 5
    # 2 1 2 3 2 4 2 5
    # 3 3 1 1 2 2 4 4 5 5
    pattern1 = [1, 2, 3, 4, 5]
    len_pattern1 = len(pattern1)
    pattern2 = [2, 1, 2, 3, 2, 4, 2, 5]
    len_pattern2 = len(pattern2)
    pattern3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    len_pattern3 = len(pattern3)
    scores = [0, 0, 0]
    winners = []

    for idx, answer in enumerate(answers):
        if answer == pattern1[idx % len_pattern1]:
            scores[0] += 1
        if answer == pattern2[idx % len_pattern2]:
            scores[1] += 1
        if answer == pattern3[idx % len_pattern3]:
            scores[2] += 1

    for idx, score in enumerate(scores):
        if score == max(scores):
            winners.append(idx + 1)

    return winners
