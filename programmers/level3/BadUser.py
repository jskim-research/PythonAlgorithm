"""
programmers 불량사용자 풀이

시작 시간: 2022.09.22 23:52
끝 시간: 2022.09.23 0:24
걸린 시간: 32분
병목 원인:
개선 여지:
"""


def match(s1, s2):  # s2가 차단 아이디로 생각
    if len(s1) != len(s2):
        return False
    for c1, c2 in zip(s1, s2):
        if c2 != '*' and c1 != c2:
            return False
    return True


def merge(l1, l2):
    ret = []
    for s1 in l1:
        for s2 in l2:
            s = s1 + s2
            if len(s) == len(set(s)):
                ret.append(s)
    return ret


def solution(user_id, banned_id):
    ban_case = []
    for b_id in banned_id:
        tmp = []
        for u_id in user_id:
            if match(u_id, b_id):
                tmp.append([u_id])
        ban_case.append(tmp)

    base = ban_case[0]
    for i in range(1, len(ban_case)):
        base = merge(base, ban_case[i])

    # sorted => 순서 고정, len(set) = len => unique pair만
    answer = set(["".join(sorted(b)) for b in base])
    return len(answer)

