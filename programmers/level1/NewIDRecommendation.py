"""
Programmers 신규 아이디 추천 풀이

시작 시간: 2022.07.17 17:48
끝 시간: 2022.07.17 18:10
걸린 시간: 22분
병목 시간: 정규 표현식 미숙
"""
import re


def solution(new_id: str):
    new_id = new_id.lower()  # 1단계
    new_id = re.sub(r"[^a-z\w\-_.]", "", new_id)  # 2단계
    new_id = re.sub(r"\.+", ".", new_id)  # 3단계
    new_id = new_id.strip(".")  # 4단계
    new_id = "a" if len(new_id) == 0 else new_id
    new_id = new_id[:15].strip(".")
    new_id = new_id + new_id[-1] * max(0, 3 - len(new_id))
    return new_id
