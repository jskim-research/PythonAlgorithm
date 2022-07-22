"""
취업을 위한 코딩테스트 왕실의 나이트 문제풀이
시작 시간: 2022.07.23 03:55
끝 시간: 2022.07.23 04:04
걸린 시간: 9분
병목 원인:
개선 방법:
"""
coord = input()
col_idx = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8}
# col_idx => int(ord(coord[0])) - int(ord('a')) + 1 로 교체 가능
cx, cy = col_idx[coord[0]], int(coord[1])

# steps = [(2, 1), (2, -1), ...] 처럼도 사용됨
dx = [2, 2, -2, -2, 1, -1, 1, -1]
dy = [1, -1, 1, -1, 2, 2, -2, -2]

possible_coords = [(cx+mx, cy+my) for mx, my in zip(dx, dy)]
available_coords = [(nx, ny) for nx, ny in possible_coords if 1 <= nx <= 8 and 1 <= ny <= 8]

print(len(available_coords))
