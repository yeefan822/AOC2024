def read_file_to_array_of_arrays(filename):
    array_of_arrays = []
    with open(filename, 'r') as file:
        for line in file:
            array_of_arrays.append(list(line.strip()))
    return array_of_arrays

def count_XMAS_times(input_array):
    count = 0
    for outer_index, array in enumerate(input_array):
        for inner_index, value in enumerate(array):
             for dir_x, dir_y in directions:
                if check_direction(inner_index, outer_index, dir_x, dir_y, input_array):
                    count += 1
    return count

def is_valid(x, y, max_rows, max_cols):
    return 0 <= x < max_rows and 0 <= y < max_cols

def check_direction(x, y, dir_x, dir_y, grid):
    for i in range(len("XMAS")):
        nx, ny = x + i * dir_x, y + i * dir_y
        if not is_valid(nx, ny, len(grid), len(grid[0])) or grid[nx][ny] != "XMAS"[i]:
            return False
    return True                

directions = [(0, 1), (1, 0), (-1, -1), (-1, 0), (1, 1), (1,-1), (0, -1), (-1, 1)]
file_path = "Data.txt"
input_array = read_file_to_array_of_arrays(file_path)
XMAS_count = count_XMAS_times(input_array)
print("XMAS appears:", XMAS_count)