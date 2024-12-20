def process_digits_from_file(file_path):
    """Reads file content as a string and processes each digit with its index."""
    with open(file_path, 'r') as file:
        content = file.read().strip()  # Read the entire file and remove any surrounding whitespace
    outputArray = []
    fileId = 0

    for index, digit in enumerate(content):
        digit = int(digit)
        
        
        if index % 2 == 0:
            outputArray.extend([fileId]*digit)
            
        else:
            outputArray.extend([-1]*digit)
            fileId += 1
            
            
    return outputArray
    
def move_file_to_front(arr):
    for i in range(len(arr) - 1, -1, -1):
        # Only consider non -1 digits
        if arr[i] != -1:
            # Find the first available `-1` from the left side
            for j in range(len(arr)):
                if arr[j] == -1 and j < i:
                    # Swap the current element with the first `-1` slot
                    arr[j], arr[i] = arr[i], arr[j]
                    break
            
    return arr


def calculate_check_sum(arr):
    sum = 0
    for index, digit in enumerate(arr):
        if digit == -1:
            break
        sum += index*digit
    return sum
    
        


file_path = 'data.txt' 
init_array = process_digits_from_file(file_path)
update_array = move_file_to_front(init_array)
print(update_array)
check_sum = calculate_check_sum(update_array)
print(check_sum)
