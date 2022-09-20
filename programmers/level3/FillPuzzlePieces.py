"""
programmers 퍼즐조각채우기 풀이

시작 시간: 2022.09.20 22:00
끝 시간: 2022.09.21 00:18
걸린 시간: 2시간 18분
병목 원인: 무엇을 먼저 회전시킬지, 각각의 case를 정리하고 문제가 없는 지 확인했어야했음.
          결과적으로 각각의 도형을 회전시켜 생기는 해의 중복보다 game_board를 회전시키면서 매칭된 block들을 메우는 방식이 효과적이었음
개선 여지:
"""


def find_block(x, y, visit, table, size, full_return=False):
    dir = [(0, 1), (1, 0), (-1, 0), (0, -1)]
    mx, my = 0, 0
    stack = [(mx, my)]
    visit[x][y] = True
    block = []
    coord = []
    while stack:
        mx, my = stack.pop()
        cx, cy = x + mx, y + my
        block.append((mx, my))
        coord.append((cx, cy))
        for (dir_x, dir_y) in dir:
            nx, ny = cx + dir_x, cy + dir_y
            if nx < 0 or nx >= size or ny < 0 or ny >= size:
                continue
            if not visit[nx][ny] and table[nx][ny] == 1:
                visit[nx][ny] = True
                stack.append((mx + dir_x, my + dir_y))
    if full_return:
        return block, coord
    else:
        return block


def rotate_matrix(mat):
    size = len(mat)
    ret_mat = [[0] * size for _ in range(size)]
    for i in range(size):
        for j in range(size):
            ret_mat[i][size - 1 - j] = mat[j][i]
    return ret_mat


def solution(game_board, table):
    # 1. find table blocks
    # 2. find game_board blocks while rotating to degree [0, 90, 180, 270]
    # 3. find matching blocks betweeen table blocks and game_board blocks
    # 4. fill the matched blocks of game_board
    # repeat 3~4
    answer = 0

    size = len(table)

    table_blocks = []
    visit = [[False] * size for _ in range(size)]
    for x in range(0, size):
        for y in range(0, size):
            if not visit[x][y] and table[x][y] == 1:
                table_block = find_block(x, y, visit, table, size)
                table_blocks.append(table_block)

    for x in range(0, size):
        for y in range(0, size):
            game_board[x][y] = 1 if game_board[x][y] == 0 else 0

    for rot in range(4):
        visit = [[False] * size for _ in range(size)]
        game_board = rotate_matrix(game_board)
        game_board_blocks = []
        game_board_coords = []
        for x in range(0, size):
            for y in range(0, size):
                if not visit[x][y] and game_board[x][y] == 1:
                    game_board_block, game_board_coord = find_block(x, y, visit, game_board, size, True)
                    game_board_blocks.append(game_board_block)
                    game_board_coords.append(game_board_coord)
        new_table_blocks = []

        for b in table_blocks:
            if b in game_board_blocks:
                answer += len(b)
                idx = game_board_blocks.index(b)
                for (x, y) in game_board_coords[idx]:
                    game_board[x][y] = 2

                # 이미 사용한 block은 사용불가능으로 설정 (100, 100은 나올 수 없는 숫자임)
                game_board_blocks[idx] = (100, 100)
                game_board_coords[idx] = (100, 100)
            else:
                new_table_blocks.append(b)
        table_blocks = new_table_blocks

    for i in range(size):
        print(game_board[i])

    return answer