

"""
[
    [0,0,1,2], 
    [0,2,2,2], 
    [2,1,0,1]
]
"""

matrix = [
    [0,0,1,2], 
    [0,2,2,2], 
    [2,1,0,1]
]


def _find_all_1s(matrix):
    results = []
    for i in range(len(matrix)):
        for j in range (len(matrix[i])):
            if matrix[i][j] == 1:
                results.append((i,j))
    return results


def check_path(direction: tuple, starting_point: tuple) -> int:
    """
    direction: tuple to increase/decrease the row where we wanna move
    starting_point: (x,y) value where start
    return: number of times the sequence was successfully
    """
    visited = 0
    current_pos = starting_point
    keep_moving = True
    while keep_moving:
        print(f" Direction: {direction}")
        try:
            next_pos_x = current_pos[0]+direction[0]
            next_pos_y = current_pos[1]+direction[1]
            print(f"  Current pos: {current_pos} - Next pos: {next_pos_x, next_pos_y}")
            print(f"    -- value: {matrix[next_pos_x][next_pos_y]}")
            if next_pos_x < 0 or next_pos_y < 0:
                print("    -- nevative index, invalid path; visited: ", visited)
                keep_moving = False
                
            # positioning on the '1' location and move one step at time
            if matrix[next_pos_x][next_pos_y] == next_val:
                print("Value is the expected one: ", next_val)
                # updated to the next
                # @todo - MOVE TO util func
                next_pos_x = next_pos_x+direction[0]
                next_pos_y = next_pos_y+direction[1]
                
                visited+=1
                if next_val==2:
                    next_val=0
                else:
                    next_val=2
            else:
                keep_moving = False
        except IndexError:
            print(f"    -- IndexError: {current_pos}")
            keep_moving = False
    return visited



def check_direction(directions):
    for direction in directions:
        while keep_moving:
            print(f" Direction: {direction}")
            try:
                next_pos_x = current_pos[0]+direction[0]
                next_pos_y = current_pos[1]+direction[1]
                print(f"  Current pos: {current_pos} - Next pos: {next_pos_x, next_pos_y}")
                print(f"    -- value: {matrix[next_pos_x][next_pos_y]}")
                if next_pos_x < 0 or next_pos_y < 0:
                    print("    -- nevative index, invalid path; visited: ", visited)
                    results.append(visited)
                    visited = 0
                    keep_moving = False
                    
                # positioning on the '1' location and move one step at time
                if matrix[next_pos_x][next_pos_y] == next_val:
                    print("Value is the expected one: ", next_val)
                    # updated to the next
                    # @todo - MOVE TO util func
                    next_pos_x = next_pos_x+direction[0]
                    next_pos_y = next_pos_y+direction[1]
                    
                    visited+=1
                    if next_val==2:
                        next_val=0
                    else:
                        next_val=2
                else:
                    keep_moving = False
                    
            except IndexError:
                print(f"    -- IndexError: {current_pos}")
                # break the nested loop, go to the next '1' position
                results.append(visited)
                visited = 0
                keep_moving = False
    
    
def solution(matrix):
    print(f"matrix: {matrix}")
    
    # to iterate over that direction until exception occurs
    directions = [(-1,-1), (1,-1), (-1,1),(1,1)]
    
    all_1s = _find_all_1s(matrix)
    print(f"all_1s_: {all_1s}")
    results = []
    for item in all_1s:
        print("Starting from: ", item)
        current_pos = (item[0], item[1])
        visited=0
        next_val=2
        #@TODO - move to separated func to break properly
        keep_moving = True
        for direction in directions:
            while keep_moving:
                print(f" Direction: {direction}")
                try:
                    next_pos_x = current_pos[0]+direction[0]
                    next_pos_y = current_pos[1]+direction[1]
                    print(f"  Current pos: {current_pos} - Next pos: {next_pos_x, next_pos_y}")
                    print(f"    -- value: {matrix[next_pos_x][next_pos_y]}")
                    if next_pos_x < 0 or next_pos_y < 0:
                        print("    -- nevative index, invalid path; visited: ", visited)
                        results.append(visited)
                        visited = 0
                        keep_moving = False
                        
                    # positioning on the '1' location and move one step at time
                    if matrix[next_pos_x][next_pos_y] == next_val:
                        print("Value is the expected one: ", next_val)
                        # updated to the next
                        # @todo - MOVE TO util func
                        next_pos_x = next_pos_x+direction[0]
                        next_pos_y = next_pos_y+direction[1]
                        
                        visited+=1
                        if next_val==2:
                            next_val=0
                        else:
                            next_val=2
                    else:
                        keep_moving = False
                        
                except IndexError:
                    print(f"    -- IndexError: {current_pos}")
                    # break the nested loop, go to the next '1' position
                    results.append(visited)
                    visited = 0
                    keep_moving = False

    print(f"results: {results}")
    print(f"longest line: {max(results)}")
    return max(results)
            
    

solution(matrix)
