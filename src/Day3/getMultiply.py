import re

def calculate_mul_sum(input_string):
    pattern = r"mul\((\d{1,3}),\s*(\d{1,3})\)"
    
    matches = re.findall(pattern, input_string)
    
    result = sum(int(x) * int(y) for x, y in matches)
    
    return result

def readFile(file_path):
    with open(file_path, 'r') as file:
        input_string = file.read()
    return input_string

    
file_path = "Data.txt"
mul_sum = calculate_mul_sum(readFile(file_path))
print("mul_sum", mul_sum)
