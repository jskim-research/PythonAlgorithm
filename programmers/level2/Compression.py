"""
programmers 압축 풀이

시작 시간: 2022.09.23 22:23
끝 시간: 2022.09.23 22:35
걸린 시간: 12분
병목 원인:
개선 여지:
"""
def solution(msg):
    m = {chr(i): i - ord('A') + 1 for i in range(ord('A'), ord('Z') + 1)}
    s = ''
    answer = []

    for c in msg:
        s += c
        if s not in m:
            # 현재 입력: s[:-1]
            # 다음 입력: s[-1]
            print(s[:-1], s[-1])
            m[s] = len(m) + 1
            answer.append(m[s[:-1]])
            s = s[-1]

    # 처리되지 않은 글자
    if s in m:
        answer.append(m[s])
    else:
        answer.append(len(m) + 1)
    return answer



