"""
취업을 위한 코딩테스트 상하좌우 문제풀이
시작 시간: 2022.07.23 03:27
끝 시간: 2022.07.23 03:33
걸린 시간: 6분
병목 원인:
개선 방법:
"""

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
command_dir = {"D": 0, "U": 1, "R": 2, "L": 3}

cx, cy = 1, 1

n = int(input())
commands = input().split()

for command in commands:
    direction = command_dir[command]
    nx, ny = cx + dx[direction], cy + dy[direction]
    if nx < 1 or nx > n or ny < 1 or ny > n:
        pass
    else:
        cx, cy = nx, ny

print(cy, cx)
