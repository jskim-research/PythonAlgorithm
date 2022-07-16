"""
programmers 신고 결과 받기 풀이
"""

import numpy as np
import typing
from collections import defaultdict


def solution(id_list: typing.List[str], report, k):
    """
    참고사항:
        각 유저는 한 번에 한 명의 유저를 신고 가능 (한 유저를 여러 번 신고할 경우 동일 유저에 대한 신고는 1회로 처리)
    Args:
        id_list: 존재하는 id들
        report:
        k:
    """
    report_info = defaultdict(set)
    reported_count = defaultdict(int)
    answer = []

    # 유저들이 신고한 유저들 정보 저장 (report_info)
    # 유저들의 누적 신고 개수 정보 저장 (reported_count)
    for r in report:
        user_id, reported_user_id = r.split(" ")
        if reported_user_id in report_info[user_id]:
            # 동일 유저에게서 2번 이상 신고받을 경우 해당 신고 무시
            pass
        else:
            # 한 유저에게서 첫 번째로 받은 신고 처리
            report_info[user_id].add(reported_user_id)
            reported_count[reported_user_id] += 1

    # 각 유저가 신고한 유저 중 실제로 ban 된 유저의 개수 세기
    for user_id in id_list:
        is_ban = list(map(lambda id: reported_count[id] >= k, list(report_info[user_id])))
        answer.append(int(np.sum(is_ban)))

    return answer


if __name__ == "__main__":
    print(solution(["muzi", "frodo", "apeach", "neo"], ["muzi frodo", "apeach frodo", "frodo neo", "muzi neo", "apeach muzi"], 2))

