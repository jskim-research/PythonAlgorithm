"""
programmers 오픈채팅방 문제풀이

시작 시간: 2022.07.21 00:58
끝 시간: 2022.07.21 01:14
걸린 시간: 16분
병목 원인: 깔끔한 코드를 짜기 위해 고민
개선 방법: comprehension 적극 활용 및 string 함수 이용
"""

"""
닉네임이 바뀌는 경우: Enter, Change
출력해야하는 경우: Enter, Leave
"""


def solution(record):
    command_print = {"Enter": "님이 들어왔습니다.", "Leave": "님이 나갔습니다."}
    id_name = {r.split()[1]: r.split()[2] for r in record if r.startswith('Enter') or r.startswith('Change')}
    answer = [f"{id_name[r.split()[1]]}{command_print[r.split()[0]]}" for r in record if not r.startswith('Change')]

    return answer

