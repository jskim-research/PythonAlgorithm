"""
취업을 위한 코딩테스트 게임 개발 문제풀이
시작 시간: 2022.07.23 04:15
끝 시간: 2022.07.23 04:45
걸린 시간: 30분
병목 원인:
개선 방법:
"""

row, col = map(int, input().split())
cy, cx, direction = map(int, input().split())
dx = [0, 1, 0, -1]  # 북, 동, 남, 서
dy = [-1, 0, 1, 0]

map_array = [list(map(int, input().split())) for i in range(row)]  # 0: 육지, 1: 바다
visit = [[0] * col for _ in range(row)]

# 시작 지점은 이미 방문한 지점
count = 1
visit[cy][cx] = 1

rotation_count = 0

while True:
    direction = (direction + 3) % 4  # 왼쪽 회전
    rotation_count += 1
    nx, ny = cx + dx[direction], cy + dy[direction]
    if visit[ny][nx] != 1 and map_array[ny][nx] != 1:
        cx, cy = nx, ny
        count += 1
        rotation_count = 0
        visit[cy][cx] = 1

    if rotation_count == 4:  # 모든 방향이 막혀있거나, 방문했던 경우 뒤로 한 칸 이동. 만약 뒤도 막혀있는 경우 종료.
        back_direction = (direction + 2) % 4
        nx, ny = cx + dx[back_direction], cy + dy[back_direction]
        rotation_count = 0
        if map_array[ny][nx] == 1:
            break
        else:
            cx, cy = nx, ny  # 이미 다 탐색했던거라 visit 처리나 count 처리는 필요없음

print(count)
