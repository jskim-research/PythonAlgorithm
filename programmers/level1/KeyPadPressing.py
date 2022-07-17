"""
programmers 키패드 누르기 풀이
"""


def dist(coord1, coord2):
    return abs(coord1[0] - coord2[0]) + abs(coord1[1] - coord2[1])


def solution(numbers, hand):
    """
    1을 (0, 0), *을 (3, 2)로 생각
    """
    number_coord = {1: [0, 0], 2: [0, 1], 3: [0, 2],
                    4: [1, 0], 5: [1, 1], 6: [1, 2],
                    7: [2, 0], 8: [2, 1], 9: [2, 2],
                    0: [3, 1]}
    left_hand_coord = [3, 0]
    right_hand_coord = [3, 2]
    answer = []

    for number in numbers:
        coord = number_coord[number]
        if number in [1, 4, 7]:
            left_hand_coord = coord
            answer.append("L")
        elif number in [3, 6, 9]:
            right_hand_coord = coord
            answer.append("R")
        else:
            dist1 = dist(left_hand_coord, coord)
            dist2 = dist(right_hand_coord, coord)
            if dist1 < dist2:
                left_hand_coord = coord
                answer.append("L")
            elif dist1 > dist2:
                right_hand_coord = coord
                answer.append("R")
            else:
                if hand == "left":
                    left_hand_coord = coord
                    answer.append("L")
                else:
                    right_hand_coord = coord
                    answer.append("R")
    return "".join(answer)