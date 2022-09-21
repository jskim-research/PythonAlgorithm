"""
programmers 단속카메라 풀이

시작 시간: 2022.09.21 22:25
끝 시간: 2022.09.21 22:31
걸린 시간: 6분
병목 원인:
개선 여지:
"""


def solution(routes):
    routes = sorted(routes, key=lambda x: x[1])
    last_pos = routes[0][1]
    camera_num = 1

    for i in range(1, len(routes)):
        if routes[i][0] <= last_pos:
            pass
        else:
            last_pos = routes[i][1]
            camera_num += 1

    return camera_num
