import re

def calculate_mul_sum(input_string):
    pattern = r"mul\((\d{1,3}),\s*(\d{1,3})\)"
    status_pattern = r"do\(\)|don't\(\)"
    enable = True 
    
    combined_pattern = re.compile(f"{pattern}|{status_pattern}")
    total_sum = 0
    
    for match in combined_pattern.finditer(input_string):
        if match.group(0).startswith("do()"):
            enable = True
        elif match.group(0).startswith("don't()"):
            enable = False
        elif match.group(1) and enable:
            total_sum += int(match.group(1)) * int(match.group(2))

    return total_sum

def readFile(file_path):
    with open(file_path, 'r') as file:
        input_string = file.read()
    return input_string

file_path = "Data.txt"
mul_sum = calculate_mul_sum(readFile(file_path))
print("Sum is", mul_sum)


