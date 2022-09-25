"""
programmers 스킬트리 풀이

시작 시간: 2022.09.25 09:10
끝 시간: 2022.09.23 09:23
걸린 시간: 13분
병목 원인:
개선 여지:
"""


def solution(skill, skill_trees):
    skill = list(skill)
    s = set(skill)
    answer = 0

    for tree in skill_trees:
        cur_skill_idx = 0
        possible = True
        tree = list(tree)
        for t in tree:
            if t in s:
                if t == skill[cur_skill_idx]:
                    cur_skill_idx += 1
                else:
                    possible = False
                    break
        if possible:
            answer += 1

    return answer