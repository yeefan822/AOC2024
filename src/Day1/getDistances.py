array1 = []
array2 = []

with open('Data.txt', 'r') as file:
    for line in file:
        value1, value2 = map(int, line.split())  # Convert the strings to integers
        array1.append(value1)  # Append the first value to array1
        array2.append(value2)  # Append the second value to array2

total_difference = sum(abs(a - b) for a, b in zip(sorted(array1), sorted(array2)))

print("Sum of absolute differences:", total_difference)