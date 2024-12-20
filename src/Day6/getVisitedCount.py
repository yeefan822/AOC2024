from guard import Guard, Direction

def read_file_to_array_of_arrays(filename):
    grid = []
    with open(filename, 'r') as file:
        for line in file:
            grid.append(list(line.strip()))
    return grid

def init_guard(grid):
    for outer_index, array in enumerate(grid):
        for inner_index, value in enumerate(array):
            if value != "." and value != "#":
                return Guard(inner_index, outer_index, Direction(value))

def game_start(grid, guard):
    visited_positions = set()
    visited_positions.add((guard.x, guard.y))

    while 0 <= guard.x < len(grid[0])-1 and 0 <= guard.y < len(grid)-1:
        next_x, next_y = guard.attempt_move()
        if grid[next_y][next_x] != "#":
            guard.move(next_x, next_y)
            #print("moved")
        else:
            guard.turn()
        visited_positions.add((guard.x, guard.y))

    return visited_positions

file_path = "Data.txt"
input_grid = read_file_to_array_of_arrays(file_path)
guard = init_guard(input_grid)
visited_positions = game_start(input_grid, guard)

print(guard.direction)
print("Number of visited positions:", len(visited_positions))