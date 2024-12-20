def read_file(file_path):
    with open(file_path, "r") as file:
    	file_content = file.read()
    lines = file_content.strip().splitlines()
    rules = []
    updates = []

    for line in lines:
        if "|" in line:
            rules.append(tuple(map(int, line.split("|"))))
        elif "," in line:
            updates.append(list(map(int, line.split(","))))

    return rules, updates

def is_correctly_ordered(update, rules):
    for a, b in rules:
        if a in update and b in update:
            if update.index(a) > update.index(b):
                return False
    return True

def find_middle_number(update):
    return update[len(update) // 2]

def solve_manual_ordering_sum_mediums(file_path):
    rules, updates = read_file(file_path)
    correct_updates = [update for update in updates if is_correctly_ordered(update, rules)]
    middle_numbers = [find_middle_number(update) for update in correct_updates]
    
    print(middle_numbers)
    return sum(middle_numbers)


file_path = "Data.txt"
sum_value = solve_manual_ordering_sum_mediums(file_path)
print("Sum of mediums:", sum_value)

