from itertools import product

def read_file_to_array_of_arrays(filename):
    with open(filename, "r") as file:
        keys = []
        values = []
        for line in file:
            key, value = line.split(":")  
            keys.append(int(key.strip()))  
            values.append(list(map(int, value.strip().split()))) 
    return keys, values

def evaluate_expression(numbers, operators):
    result = numbers[0]
    for i, op in enumerate(operators):
        if op == '+':
            result += numbers[i + 1]
        elif op == '*':
            result *= numbers[i + 1]
    return result

def calculate_calibration_result(sums, numbers):
    total_calibration_result = 0

    for aggregation, numbers in zip(sums, numbers):
        num_positions = len(numbers) - 1
        all_operator_combinations = product("+-*", repeat=num_positions)

        for operators in all_operator_combinations:
            result = evaluate_expression(numbers, operators)
            if result == aggregation:
                total_calibration_result += aggregation
                break

    return total_calibration_result

file_path = "Data.txt"
sums, numbers = read_file_to_array_of_arrays(file_path)
result = calculate_calibration_result(sums, numbers)

print("Number of visited positions:", result)