matrix = [[0,0,1,2], [0,2,2,2], [2,1,0,1]]

def _find_all_1s(matrix):
    results = []
    for i in range(len(matrix)):
        for j in range (len(matrix[i])):
            if matrix[i][j] == 1:
                results.append((i,j))
    return results


def check_path(direction: tuple, starting_point: tuple) -> int:
    visited = 0
    next_val = 2
    current_pos = starting_point
    keep_moving = True
    while keep_moving:
        try:
            next_pos_x = current_pos[0]+direction[0]
            next_pos_y = current_pos[1]+direction[1]
            if next_pos_x < 0 or next_pos_y < 0:
                keep_moving = False
                break
            # positioning on the '1' location and move one step at time
            _value = matrix[next_pos_x][next_pos_y]
            if _value == next_val:
                current_pos = (next_pos_x, next_pos_y)
                visited+=1
                if next_val==2:
                    next_val=0
                else:
                    next_val=2
            else:
                keep_moving = False
        except IndexError:
            keep_moving = False
    return visited


def check_direction(starting_point: tuple, directions):
    results = []
    for direction in directions:
        results.append(check_path(direction, starting_point))
    return results


def solution(matrix):
    directions = [(-1,-1), (1,-1), (-1,1),(1,1)]
    all_1s = _find_all_1s(matrix)
    results = []
    for item in all_1s:
        results.extend(check_direction(item, directions))
    return max(results)

solution(matrix)