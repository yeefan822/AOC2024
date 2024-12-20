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
            if check_MAS_pattern(inner_index, outer_index, input_array):
                count += 1
    return count

def is_valid(x, y, max_rows, max_cols):
    return 0 <= x+1 < max_rows and 0 <= y+1 < max_cols and 0 <= x-1 < max_rows and 0 <= y-1 < max_cols 


def check_MAS_pattern(x, y, grid):
    if(grid[x][y] == "A" and is_valid(x, y, len(grid), len(grid[0]))):
        if(grid[x-1][y+1] == "M"):
            if(grid[x+1][y-1] == "S"):
                if(grid[x-1][y-1] == "S" and grid[x+1][y+1] == "M"):
                    return True
                if(grid[x+1][y+1] == "S" and grid[x-1][y-1] == "M"):
                    return True
            else:
                return False
        if(grid[x-1][y+1] == "S"):
            if(grid[x+1][y-1] == "M"):
                if(grid[x-1][y-1] == "M" and grid[x+1][y+1] == "S"):
                    return True
                if(grid[x+1][y+1] == "M" and grid[x-1][y-1] == "S"):
                    return True
            else:
                return False
    return False
            


file_path = "Data.txt"
input_array = read_file_to_array_of_arrays(file_path)
XMAS_count = count_XMAS_times(input_array)
print("XMAS appears:", XMAS_count)


